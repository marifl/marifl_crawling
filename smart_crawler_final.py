#!/usr/bin/env python3
"""
Funktionierender Smart Website Crawler mit korrekter Kapitel-Reihenfolge und dynamischem Padding
"""
import asyncio
import argparse
import sys
import re
import json
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests
import html2text
from crawl4ai import AsyncWebCrawler
from typing import List, Tuple, Optional


class SmartCrawler:
    def __init__(self, delay: float = 0, timeout: int = 30, max_retries: int = 3):
        self.chapter_order: List[Tuple[str, str, str]] = []
        self.filename_mapping: dict = {}  # Mapping von URLs zu Dateinamen
        self.delay = delay
        self.timeout = timeout
        self.max_retries = max_retries
        self.skip_existing = False
        self.dry_run = False
        self.include_nav = True
        self.clean_output = False
    
    def extract_navigation_order(self, start_url: str) -> List[Tuple[str, str, str]]:
        """Extrahiert die korrekte Kapitel-Reihenfolge aus der Navigation"""
        print(f"🔍 Analysiere Navigation von {start_url}")
        
        try:
            response = requests.get(start_url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # URL-Basis für Filterung
            parsed = urlparse(start_url)
            base_domain = parsed.netloc
            base_path = '/'.join(parsed.path.split('/')[:-1]) + '/' if parsed.path else '/'
            
            chapter_order = []
            
            # Navigation finden - alle Links die zu HTML-Seiten führen
            nav_links = soup.find_all('a', href=True)
            
            for link in nav_links:
                href = link.get('href')
                if not href or not isinstance(href, str):
                    continue
                    
                # Nur .html Links berücksichtigen
                if not href.endswith('.html'):
                    continue
                    
                # Vollständige URL erstellen
                if href.startswith('/'):
                    full_url = f"https://{base_domain}{href}"
                elif href.startswith('http'):
                    full_url = href
                else:
                    full_url = urljoin(start_url, href)
                
                # Nur Links aus derselben Domain und Pfad
                if not (base_domain in full_url and base_path in full_url):
                    continue
                    
                # Fragment entfernen
                clean_url = full_url.split('#')[0]
                
                # Text des Links extrahieren
                link_text = link.get_text(strip=True)
                
                # Kapitelnummer extrahieren falls vorhanden
                chapter_match = re.search(r'(\d+(?:\.\d+)*)', link_text)
                chapter_number = chapter_match.group(1) if chapter_match else ""
                
                # Titel bereinigen (Kapitelnummer entfernen)
                clean_title = re.sub(r'^\d+(?:\.\d+)*\s*', '', link_text).strip()
                
                if clean_url not in [item[0] for item in chapter_order]:
                    chapter_order.append((clean_url, chapter_number, clean_title))
            
            # Nach Kapitelnummer sortieren
            def sort_key(item):
                url, chapter_num, title = item
                if chapter_num:
                    # Kapitelnummer in sortierbare Form umwandeln
                    parts = [int(x) for x in chapter_num.split('.')]
                    while len(parts) < 5:
                        parts.append(0)
                    return parts
                else:
                    # Seiten ohne Kapitelnummer kommen zuerst
                    return [-1, 0, 0, 0, 0]
            
            chapter_order.sort(key=sort_key)
            
            print(f"📄 Gefundene Kapitel-Reihenfolge:")
            for i, (url, chapter_num, title) in enumerate(chapter_order):
                # Anzeige: 0 für unnummerierte Seiten, echte Kapitelnummer für nummerierte
                display_index = int(chapter_num) if chapter_num else 0
                print(f"  {display_index:2d}. {chapter_num:>4s} - {title}")
            
            return chapter_order
            
        except Exception as e:
            print(f"❌ Fehler beim Extrahieren der Navigation: {e}")
            return []
    
    async def save_as_html(self, url: str, filename: str, output_dir: Path) -> bool:
        """Speichert eine URL als HTML"""
        # Skip if file exists and skip_existing is True
        file_path = output_dir / filename
        if self.skip_existing and file_path.exists():
            print(f"⏭️  Überspringe existierende Datei: {filename}")
            return True
            
        # Dry run mode
        if self.dry_run:
            print(f"🔍 [DRY RUN] Würde speichern: {filename}")
            return True
            
        try:
            async with AsyncWebCrawler(verbose=False, timeout=self.timeout) as crawler:
                result = await crawler.arun(url=url)
                
                if hasattr(result, 'success') and result.success:
                    soup = BeautifulSoup(result.html, 'html.parser')
                    
                    # Copy-Buttons entfernen
                    for copy_btn in soup.select('.copy, .copy-button, .btn-copy, .fa-copy, button[title="Copy"]'):
                        copy_btn.decompose()
                    
                    # Navigation entfernen wenn gewünscht
                    if not self.include_nav:
                        for nav in soup.select('nav, .navigation, .nav, .sidebar, .toc, aside'):
                            nav.decompose()
                    
                    # Clean output - entferne Scripts, Styles, etc.
                    if self.clean_output:
                        for element in soup.select('script, style, meta, link[rel="stylesheet"]'):
                            element.decompose()
                    
                    # Links korrigieren
                    soup = self.fix_internal_links_html(soup)
                    
                    # HTML mit Kommentar speichern
                    html_content = f"<!-- Original URL: {url} -->\n{str(soup)}"
                    
                    file_path = output_dir / filename
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    return True
                else:
                    print(f"❌ Crawl4ai Fehler für {url}")
                    return False
                    
        except Exception as e:
            print(f"❌ Fehler beim Speichern von {url}: {e}")
            return False
    
    def fix_internal_links_html(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Konvertiert interne Links in HTML-Dokumenten zu den neuen Dateinamen"""
        # Erstelle Mapping von original HTML-Dateinamen zu neuen Dateinamen
        for url, chapter_num, title in self.chapter_order:
            # Extrahiere HTML-Dateiname aus URL
            original_filename = url.split('/')[-1]
            # Generiere neuen Dateinamen
            new_filename = self.generate_filename(chapter_num, title, 'html', len(self.chapter_order))
            self.filename_mapping[original_filename] = new_filename
        
        # Ersetze alle Links
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href and isinstance(href, str):
                # Extrahiere Dateiname und Anker
                if '#' in href:
                    filename, anchor = href.split('#', 1)
                    anchor = '#' + anchor
                else:
                    filename = href
                    anchor = ''
                
                # Wenn es ein lokaler Link ist
                if filename.endswith('.html') and not filename.startswith('http'):
                    # Finde entsprechenden neuen Dateinamen
                    if filename in self.filename_mapping:
                        link['href'] = self.filename_mapping[filename] + anchor
        
        return soup
    
    def fix_internal_links(self, content: str, format_type: str) -> str:
        """Konvertiert interne Links von .html zu .md Dateinamen"""
        if format_type != 'md':
            return content
            
        # Erstelle Mapping von HTML-Dateinamen zu MD-Dateinamen
        for url, chapter_num, title in self.chapter_order:
            # Extrahiere HTML-Dateiname aus URL
            html_filename = url.split('/')[-1]
            # Generiere entsprechenden MD-Dateinamen
            md_filename = self.generate_filename(chapter_num, title, 'md', len(self.chapter_order))
            self.filename_mapping[html_filename] = md_filename
        
        # Ersetze alle Links
        import re
        
        def replace_link(match):
            full_match = match.group(0)
            text = match.group(1)
            link = match.group(2)
            
            # Extrahiere Dateiname und Anker
            if '#' in link:
                filename, anchor = link.split('#', 1)
                anchor = '#' + anchor
            else:
                filename = link
                anchor = ''
            
            # Wenn es ein interner Link ist (endet mit .html oder .md)
            if filename.endswith('.html'):
                # Finde entsprechenden MD-Dateinamen
                if filename in self.filename_mapping:
                    new_filename = self.filename_mapping[filename]
                    return f'[{text}]({new_filename}{anchor})'
            elif filename.endswith('.md'):
                # Finde den ursprünglichen HTML-Dateinamen für diesen MD-Link
                # Suche in chapter_order nach einem passenden Titel
                for url, chapter_num, chapter_title in self.chapter_order:
                    # Generiere den erwarteten alten MD-Dateinamen basierend auf dem Titel
                    # Dies ist eine Heuristik - wir versuchen den Titel aus dem Dateinamen zu extrahieren
                    if filename.replace('.md', '').replace('_', ' ').lower() in chapter_title.lower():
                        # Generiere neuen Dateinamen
                        new_filename = self.generate_filename(chapter_num, chapter_title, 'md', len(self.chapter_order))
                        return f'[{text}]({new_filename}{anchor})'
                
                # Wenn keine Übereinstimmung gefunden wurde, versuche über den Index
                # Extrahiere Nummer aus dem Dateinamen wenn vorhanden
                number_match = re.match(r'^(\d+)', filename)
                if number_match:
                    target_num = number_match.group(1).lstrip('0') or '0'
                    for url, chapter_num, chapter_title in self.chapter_order:
                        if chapter_num == target_num:
                            new_filename = self.generate_filename(chapter_num, chapter_title, 'md', len(self.chapter_order))
                            return f'[{text}]({new_filename}{anchor})'
            
            return full_match
        
        # Ersetze Links in Markdown-Format: [Text](link)
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
        
        # Ersetze auch direkte Links in Klammern: (link)
        content = re.sub(r'\(([^)]+\.html(?:#[^)]+)?)\)', 
                        lambda m: '(' + self.filename_mapping.get(m.group(1).split('#')[0], m.group(1)) + 
                        (('#' + m.group(1).split('#')[1]) if '#' in m.group(1) else '') + ')', 
                        content)
        
        # Spezialfall: Links die mit ./ beginnen (relative Links zum Root)
        content = re.sub(r'\[([^\]]+)\]\(\.\/\)', r'[\1](index.md)', content)
        
        return content
    
    async def save_as_markdown(self, url: str, filename: str, output_dir: Path) -> bool:
        """Speichert eine URL als Markdown"""
        # Skip if file exists and skip_existing is True
        file_path = output_dir / filename
        if self.skip_existing and file_path.exists():
            print(f"⏭️  Überspringe existierende Datei: {filename}")
            return True
            
        # Dry run mode
        if self.dry_run:
            print(f"🔍 [DRY RUN] Würde speichern: {filename}")
            return True
            
        try:
            async with AsyncWebCrawler(verbose=False, timeout=self.timeout) as crawler:
                result = await crawler.arun(url=url)
                
                if hasattr(result, 'success') and result.success:
                    h = html2text.HTML2Text()
                    h.ignore_links = False
                    h.ignore_images = False
                    h.body_width = 0
                    h.unicode_snob = True
                    
                    soup = BeautifulSoup(result.html, 'html.parser')
                    
                    # Copy-Buttons entfernen
                    for copy_btn in soup.select('.copy, .copy-button, .btn-copy, .fa-copy, button[title="Copy"]'):
                        copy_btn.decompose()
                    
                    # Navigation entfernen wenn gewünscht
                    if not self.include_nav:
                        for nav in soup.select('nav, .navigation, .nav, .sidebar, .toc, aside'):
                            nav.decompose()
                    
                    # Clean output - entferne Scripts, Styles, etc.
                    if self.clean_output:
                        for element in soup.select('script, style, meta, link'):
                            element.decompose()
                    
                    markdown_content = h.handle(str(soup))
                    
                    # Links korrigieren - NACH der Konvertierung zu Markdown
                    markdown_content = self.fix_internal_links(markdown_content, 'md')
                    
                    content_with_meta = f"<!-- Original URL: {url} -->\n\n{markdown_content}"
                    
                    # Create index.md for the root link
                    if filename == self.generate_filename("", "Über dieses Skript", 'md', len(self.chapter_order)):
                        index_content = f"<!-- Original URL: {url} -->\n\n# Index\n\nThis is the main index page. Start reading from [Über dieses Skript]({filename}).\n"
                        index_path = output_dir / "index.md"
                        with open(index_path, 'w', encoding='utf-8') as f:
                            f.write(index_content)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content_with_meta)
                    
                    return True
                else:
                    print(f"❌ Crawl4ai Fehler für {url}")
                    return False
                    
        except Exception as e:
            print(f"❌ Fehler beim Speichern von {url}: {e}")
            return False
    
    def generate_filename(self, chapter_num: str, title: str, format_type: str, total_chapters: int) -> str:
        """Generiert einen Dateinamen mit dynamischem Padding"""
        safe_title = re.sub(r'[^\w\s\-_\u00C0-\u017F]', '', title)
        safe_title = re.sub(r'\s+', '_', safe_title)[:40]
        
        # Dynamisches Padding basierend auf Gesamtanzahl
        if total_chapters < 10:
            padding = 1
        elif total_chapters < 100:
            padding = 2
        elif total_chapters < 1000:
            padding = 3
        else:
            padding = 4
        
        if chapter_num:
            # Nummerierte Kapitel
            padded_chapter = chapter_num.zfill(padding)
            filename = f"{padded_chapter}_{safe_title}" if safe_title else f"{padded_chapter}_Page"
        else:
            # Unnummerierte Seiten bekommen Nullen
            zero_prefix = "0" * padding
            filename = f"{zero_prefix}_{safe_title}" if safe_title else f"{zero_prefix}_Page"
        
        extension = '.html' if format_type == 'html' else '.md'
        return filename + extension
    
    def create_index_file(self, chapter_order: List[Tuple[str, str, str]], format_type: str, output_dir: Path) -> None:
        """Erstellt eine Index-Datei mit der Zuordnung von Dateinamen zu URLs"""
        index_data = {
            "format": format_type,
            "total_chapters": len(chapter_order),
            "files": []
        }
        
        # Für jedes Kapitel die Zuordnung erstellen
        for i, (url, chapter_num, title) in enumerate(chapter_order):
            filename = self.generate_filename(chapter_num, title, format_type, len(chapter_order))
            index_data["files"].append({
                "filename": filename,
                "url": url,
                "chapter_number": chapter_num,
                "title": title,
                "index": i
            })
        
        # Index-Datei speichern
        index_path = output_dir / "index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)
        
        print(f"📋 Index-Datei erstellt: {index_path}")
        
        # Zusätzlich eine lesbare Markdown-Übersicht erstellen
        readme_path = output_dir / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(f"# Crawling Index\n\n")
            f.write(f"**Format:** {format_type}\n")
            f.write(f"**Total Chapters:** {len(chapter_order)}\n\n")
            f.write("## Files\n\n")
            f.write("| Filename | Chapter | Title | URL |\n")
            f.write("|----------|---------|-------|-----|\n")
            
            for item in index_data["files"]:
                chapter = item["chapter_number"] or "0"
                f.write(f"| {item['filename']} | {chapter} | {item['title']} | {item['url']} |\n")
        
        print(f"📄 README erstellt: {readme_path}")
    
    async def crawl_website(self, start_url: str, output_dir: str, format_type: str, 
                           skip_existing: bool = False, dry_run: bool = False,
                           include_nav: bool = True, clean_output: bool = False,
                           filter_pattern: Optional[str] = None, max_pages: Optional[int] = None):
        """Hauptfunktion zum intelligenten Crawlen"""
        self.skip_existing = skip_existing
        self.dry_run = dry_run
        self.include_nav = include_nav
        self.clean_output = clean_output
        
        output_path = Path(output_dir)
        if not self.dry_run:
            output_path.mkdir(parents=True, exist_ok=True)
        
        # Kapitel-Reihenfolge extrahieren
        chapter_order = self.extract_navigation_order(start_url)
        
        if not chapter_order:
            print("❌ Keine Kapitel gefunden!")
            return
        
        # Filter anwenden wenn gewünscht
        if filter_pattern:
            pattern = re.compile(filter_pattern, re.IGNORECASE)
            filtered_order = [(url, num, title) for url, num, title in chapter_order 
                             if pattern.search(title) or pattern.search(url)]
            print(f"🔍 Filter '{filter_pattern}' angewendet: {len(filtered_order)}/{len(chapter_order)} Seiten")
            chapter_order = filtered_order
        
        # Begrenzen auf max_pages wenn gewünscht
        if max_pages and max_pages > 0:
            chapter_order = chapter_order[:max_pages]
            print(f"📄 Limitiert auf {max_pages} Seiten")
        
        # Chapter order speichern für Link-Konvertierung
        self.chapter_order = chapter_order
        
        # Index-Datei erstellen BEVOR das Crawling beginnt
        if not self.dry_run:
            self.create_index_file(chapter_order, format_type, output_path)
        
        # Jede URL crawlen
        success_count = 0
        start_time = time.time()
        
        for i, (url, chapter_num, title) in enumerate(chapter_order, 1):
            filename = self.generate_filename(chapter_num, title, format_type, len(chapter_order))
            print(f"[{i:2d}/{len(chapter_order)}] Crawle: {title}")
            print(f"                     URL: {url}")
            
            # Retry logic
            success = False
            for retry in range(self.max_retries):
                if retry > 0:
                    print(f"   🔄 Wiederholung {retry}/{self.max_retries - 1}")
                
                if format_type == 'html':
                    success = await self.save_as_html(url, filename, output_path)
                else:
                    success = await self.save_as_markdown(url, filename, output_path)
                
                if success:
                    break
                    
                # Wait before retry
                if retry < self.max_retries - 1:
                    await asyncio.sleep(self.delay * 2)
            
            if success:
                print(f"✅ Gespeichert: {filename}")
                success_count += 1
            else:
                print(f"❌ Fehler bei: {filename}")
            
            # Delay zwischen Requests
            if self.delay > 0 and i < len(chapter_order):
                print(f"⏱️  Warte {self.delay}s...")
                await asyncio.sleep(self.delay)
        
        elapsed_time = time.time() - start_time
        
        print("-" * 70)
        print(f"🎉 Intelligentes Crawling abgeschlossen!")
        print(f"   Erfolgreich: {success_count}/{len(chapter_order)} Seiten")
        print(f"   Zeit: {elapsed_time:.1f}s")
        if not self.dry_run:
            print(f"   Gespeichert in: {output_path}")
            print(f"   Index-Datei: {output_path / 'index.json'}")
            print(f"   Übersicht: {output_path / 'README.md'}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Intelligenter Website Crawler mit erweiterten Optionen",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  # Normale Verwendung
  %(prog)s -u https://example.com/docs -o output -F md
  
  # Mit Verzögerung zwischen Requests
  %(prog)s -u https://example.com/docs -o output -F md -d 1.0
  
  # Nur neue Dateien crawlen
  %(prog)s -u https://example.com/docs -o output -F md -s
  
  # Dry-run um zu sehen was gecrawlt würde
  %(prog)s -u https://example.com/docs -o output -F md -n
  
  # Nur bestimmte Kapitel crawlen
  %(prog)s -u https://example.com/docs -o output -F md -f "installation|setup"
  
  # Begrenzt auf 10 Seiten mit sauberem Output
  %(prog)s -u https://example.com/docs -o output -F md -m 10 -c
        """
    )
    
    # Erforderliche Argumente
    required = parser.add_argument_group('erforderliche Argumente')
    required.add_argument('-u', '--url', required=True,
                         help='Start-URL der zu crawlenden Website')
    required.add_argument('-o', '--output', required=True,
                         help='Output-Verzeichnis für die gespeicherten Dateien')
    required.add_argument('-f', '--format', required=True, choices=['html', 'md'],
                         help='Output-Format (html oder md)')
    
    # Optionale Argumente
    optional = parser.add_argument_group('optionale Argumente')
    optional.add_argument('-d', '--delay', type=float, default=0.0,
                         help='Verzögerung in Sekunden zwischen Requests (Standard: 0)')
    
    optional.add_argument('-t', '--timeout', type=int, default=30,
                         help='Timeout in Sekunden für jeden Request (Standard: 30)')
    
    optional.add_argument('-r', '--max-retries', type=int, default=3,
                         help='Maximale Anzahl von Wiederholungen bei Fehlern (Standard: 3)')
    
    optional.add_argument('-s', '--skip-existing', action='store_true',
                         help='Überspringe bereits existierende Dateien')
    
    optional.add_argument('-n', '--dry-run', action='store_true',
                         help='Simulation ohne tatsächliches Speichern (zeigt nur was gemacht würde)')
    
    optional.add_argument('-N', '--no-navigation', action='store_true',
                         help='Entfernt Navigations-Elemente aus dem Output')
    
    optional.add_argument('-c', '--clean', action='store_true',
                         help='Entfernt Scripts, Styles und Meta-Tags für saubereren Output')
    
    optional.add_argument('-fil', '--filter', type=str, dest='filter_pattern',
                         help='Regex-Filter für Seitentitel oder URLs')
    
    optional.add_argument('-m', '--max-pages', type=int,
                         help='Maximale Anzahl von Seiten die gecrawlt werden sollen')
    
    optional.add_argument('-v', '--verbose', action='store_true',
                         help='Detaillierte Debug-Informationen')
    
    return parser.parse_args()


def main():
    """Hauptfunktion für den Smart Crawler."""
    args = parse_arguments()
    
    # Konfiguration anzeigen
    print("-" * 70)
    print("🤖 Smart Website Crawler")
    print("-" * 70)
    print(f"   URL: {args.url}")
    print(f"   Output: {args.output}")
    print(f"   Format: {args.format}")
    
    # Optionen
    if args.delay > 0:
        print(f"   Delay: {args.delay}s")
    if args.skip_existing:
        print(f"   Skip existing: ✓")
    if args.dry_run:
        print(f"   Mode: DRY RUN")
    if args.no_navigation:
        print(f"   Navigation: ✗")
    if args.clean:
        print(f"   Clean output: ✓")
    if args.filter_pattern:
        print(f"   Filter: {args.filter_pattern}")
    if args.max_pages:
        print(f"   Max pages: {args.max_pages}")
        
    print("-" * 70)
    
    try:
        crawler = SmartCrawler(
            delay=args.delay,
            timeout=args.timeout,
            max_retries=args.max_retries
        )
        
        asyncio.run(crawler.crawl_website(
            args.url, 
            args.output, 
            args.format,
            skip_existing=args.skip_existing,
            dry_run=args.dry_run,
            include_nav=not args.no_navigation,
            clean_output=args.clean,
            filter_pattern=args.filter_pattern,
            max_pages=args.max_pages
        ))
        
        print("✅ Smart crawling completed successfully!")
        
    except KeyboardInterrupt:
        print("\n❌ Smart crawling interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error during smart crawling: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

    def advanced_filtering(self, content: str) -> str:
        """Erweiterte Filterung - noch nicht implementiert"""
        # TODO: Implementierung folgt
        return content  # Stub - gibt Input unverändert zurück

    def export_to_pdf(self, files: List[str]) -> None:
        """PDF Export - Stub für zukünftige Funktion"""
        raise NotImplementedError("PDF Export noch nicht implementiert")
