# 📋 Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

## [Unveröffentlicht]

### Geplant
- PDF-Export Funktionalität
- GUI-Interface für weniger technische Nutzer
- Erweiterte Konfigurationsdateien
- Plugin-System für Erweiterungen

## [1.0.0] - 2025-06-30

### 🎉 Erstes Release

#### Hinzugefügt
- **Intelligenter Website-Crawler** speziell für Bookdown-Seiten
- **Automatische Navigationsanalyse** mit korrekter Kapitelreihenfolge
- **Mehrere Ausgabeformate**: HTML und Markdown
- **Dynamische Dateinummerierung** basierend auf Gesamtanzahl der Seiten
- **Link-Korrektur** für interne Verlinkungen zwischen Kapiteln
- **Erweiterte CLI-Optionen**:
  - Verzögerung zwischen Anfragen (`-d, --delay`)
  - Timeout-Konfiguration (`-t, --timeout`)
  - Wiederholungslogik (`-r, --max-retries`)
  - Überspringen existierender Dateien (`-s, --skip-existing`)
  - Dry-run Modus (`-n, --dry-run`)
  - Saubere Ausgabe (`-c, --clean`)
  - Navigation entfernen (`-N, --no-navigation`)
  - Regex-Filter (`-fil, --filter`)
  - Seitenbegrenzung (`-m, --max-pages`)
  - Verbose-Modus (`-v, --verbose`)

#### Technische Features
- **UV-Package-Manager** Unterstützung für moderne Python-Entwicklung
- **Globale Tool-Installation** mit `uv tool install`
- **Crawl4ai Integration** für robustes Web-Crawling
- **Beautiful Soup** für HTML-Parsing
- **html2text** für Markdown-Konvertierung
- **Automatische Index-Erstellung** (JSON und Markdown)
- **Intelligente Fehlerbehandlung** mit Retry-Logik
- **Fortschrittsverfolgung** mit detaillierter Ausgabe

#### Bookdown-spezifische Features
- ✅ Erkennt automatisch Bookdown-Navigation
- ✅ Bewahrt Kapitelreihenfolge bei
- ✅ Korrigiert interne Links zwischen Kapiteln
- ✅ Entfernt Bookdown-spezifische UI-Elemente
- ✅ Optimiert für typische Bookdown-Strukturen

#### Dokumentation
- **README.md** mit umfassender Projektdokumentation
- **INSTRUCTIONS.md** mit Schritt-für-Schritt Tutorials
- **CONTRIBUTING.md** für Entwicklerbeiträge
- **CODE_OF_CONDUCT.md** für Community-Standards
- **SECURITY.md** für Sicherheitsrichtlinien
- **SUPPORT.md** für Hilfe und Support
- **LICENSE.md** mit MIT-Lizenz
- **CHANGELOG.md** für Versionshistorie
- **ASCII-Art Kommentare** im Code für bessere Navigation

#### Beispiele und Use Cases
- **R for Data Science** (`https://r4ds.had.co.nz/`)
- **R Markdown Guide** (`https://bookdown.org/yihui/rmarkdown/`)
- **Akademische Bücher** mit Kapitelfilterung
- **Große Dokumentations-Sites** mit Resume-Funktionalität

### 🛠️ Technische Details

#### Abhängigkeiten
- **Python 3.10+** erforderlich
- **crawl4ai** für Web-Crawling
- **beautifulsoup4** für HTML-Parsing
- **html2text** für Markdown-Konvertierung
- **requests** für HTTP-Anfragen
- **uv** als Package-Manager (empfohlen)

#### Installation
```bash
# Repository klonen
git clone https://github.com/marifl/marifl_crawling.git
cd marifl_crawling

# Mit uv installieren (empfohlen)
uv sync
uv run crawl4ai-setup
uv tool install .

# Mit pip installieren
pip install -e .
python -m crawl4ai.install
```

#### Grundlegende Nutzung
```bash
# Bookdown-Seite als Markdown crawlen
scrwl -u https://r4ds.had.co.nz/index.html -o ./r4ds -f md -d 1.0 -c -N

# Mit Filterung für spezifische Kapitel
scrwl -u https://example.bookdown.org/book/ -o ./book -f md -fil "introduction|conclusion"
```

### 🐛 Bekannte Einschränkungen
- Erfordert Playwright-Browser-Setup via `crawl4ai-setup`
- JavaScript-abhängige Inhalte können problematisch sein
- Große Websites können viel Speicher verbrauchen
- Rate-Limiting abhängig von Ziel-Website

### 🙏 Danksagungen
- **[crawl4ai](https://github.com/unclecode/crawl4ai)** für robustes Web-Crawling
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)** für HTML-Parsing
- **[html2text](https://github.com/Alir3z4/html2text/)** für Markdown-Konvertierung
- **GitHub Copilot** für Entwicklungsunterstützung

---

## Versionsformat

- **[Major]**: Große, breaking changes
- **[Minor]**: Neue Features, rückwärts kompatibel  
- **[Patch]**: Bugfixes, kleine Verbesserungen

## Kategorien

- **Hinzugefügt** für neue Features
- **Geändert** für Änderungen an existierender Funktionalität
- **Veraltet** für Features, die bald entfernt werden
- **Entfernt** für entfernte Features
- **Behoben** für Bugfixes
- **Sicherheit** bei Sicherheitslücken

## Links

- [Keep a Changelog](https://keepachangelog.com/de/1.0.0/)
- [Semantic Versioning](https://semver.org/lang/de/)
- [GitHub Releases](https://github.com/marifl/marifl_crawling/releases)
