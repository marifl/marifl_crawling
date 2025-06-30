# 🕷️ marifl_crawling - Smart Website Crawler

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Ein leistungsstarker, intelligenter Website-Crawler, der die richtige Kapitelreihenfolge aus der Website-Navigation beibehält. Entwickelt mit `crawl4ai` für robuste Crawling-Funktionen.

> 🤖 Dieses Projekt wurde in Zusammenarbeit mit GitHub Copilot entwickelt

## ✨ Funktionen

- 🧠 **Intelligente Navigationsanalyse**: Extrahiert und bewahrt automatisch die richtige Kapitelreihenfolge aus der Website-Navigation
- 📑 **Mehrere Ausgabeformate**: Du kannst nach HTML oder Markdown exportieren
- 🔢 **Intelligente Dateinummerierung**: Dynamische Pufferung basierend auf der Gesamtanzahl der Seiten
- 🔗 **Link-Erhaltung**: Aktualisiert automatisch interne Links, um mit den neuen Dateinamen übereinzustimmen
- 🚀 **Erweiterte Optionen**: Wiederholungslogik, Ratenbegrenzung, Filterung und mehr
- 📊 **Fortschrittsverfolgung**: Echtzeit-Fortschrittsupdates und detaillierte Protokollierung
- 🗂️ **Indexerstellung**: Erstellt JSON-Index und Markdown-Übersicht des gecrawlten Inhalts

## 📋 Voraussetzungen

- Python 3.13 oder höher
- Abhängigkeiten werden über `pyproject.toml` verwaltet

## 🚀 Installation

### Mit uv (Empfohlen)

```bash
# Repository klonen
git clone https://github.com/marifl/marifl_crawling.git
cd marifl_crawling

# Mit uv installieren
uv sync

# Der Befehl 'scrwl' ist nach der Installation verfügbar
```

### Mit pip

```bash
# Repository klonen
git clone https://github.com/marifl/marifl_crawling.git
cd marifl_crawling

# Im Entwicklungsmodus installieren
pip install -e .
```

## 📖 Verwendung

### Grundlegende Verwendung

```bash
# Eine Website crawlen und als HTML speichern
scrwl -u https://example.com/docs/index.html -o ./output -f html

# Crawlen und als Markdown speichern
scrwl -u https://example.com/docs/index.html -o ./output -f md
```

### Erweiterte Verwendung

```bash
# Mit Verzögerung zwischen den Anfragen (empfohlen für große Seiten)
scrwl -u https://example.com/docs -o ./output -f md -d 0.5

# Vorhandene Dateien überspringen (nützlich zum Fortsetzen unterbrochener Crawls)
scrwl -u https://example.com/docs -o ./output -f md -s

# Trockenlauf, um eine Vorschau darauf zu erhalten, was gecrawlt werden würde
scrwl -u https://example.com/docs -o ./output -f md -n

# Ausgabe bereinigen (entfernt Skripte, Stile, Metatags)
scrwl -u https://example.com/docs -o ./output -f md -c

# Navigationselemente aus der Ausgabe entfernen
scrwl -u https://example.com/docs -o ./output -f md -N

# Seiten nach Regex-Muster filtern
scrwl -u https://example.com/docs -o ./output -f md -fil "chapter-[1-3]|introduction"

# Begrenzung auf die ersten 10 Seiten
scrwl -u https://example.com/docs -o ./output -f md -m 10

# Kombination mehrerer Optionen
scrwl -u https://example.com/docs -o ./output -f md -d 1.0 -c -N -m 20
```

### Anwendungsbeispiele

```bash
# Eine Bookdown-Seite mit sauberem Markdown-Ausgang crawlen
scrwl -u https://bookdown.org/yihui/rmarkdown/index.html -o ./rmarkdown_book -f md -d 0.5 -c

# Dokumentation mit bestimmten Kapiteln nur crawlen
scrwl -u https://docs.python.org/3/tutorial/index.html -o ./python_tutorial -f md -fil "introduction|data-structures|classes" -c

# Einen unterbrochenen Crawl fortsetzen
scrwl -u https://large-docs.example.com -o ./large_docs -f html -s -d 1.0
```

## 🛠️ Befehlszeilenoptionen

### Erforderliche Argumente

| Option | Beschreibung |
|--------|-------------|
| `-u, --url` | Start-URL der zu crawlenden Website |
| `-o, --output` | Ausgabeverzeichnis für gespeicherte Dateien |
| `-f, --format` | Ausgabeformat: `html` oder `md` |

### Optionale Argumente

| Option | Beschreibung | Standard |
|--------|-------------|---------|
| `-d, --delay` | Verzögerung in Sekunden zwischen den Anfragen | 0 |
| `-t, --timeout` | Timeout in Sekunden für jede Anfrage | 30 |
| `-r, --max-retries` | Maximale Anzahl von Wiederholungsversuchen für fehlgeschlagene Anfragen | 3 |
| `-s, --skip-existing` | Dateien überspringen, die bereits existieren | False |
| `-n, --dry-run` | Vorschau darauf, was gecrawlt werden würde, ohne zu speichern | False |
| `-N, --no-navigation` | Navigationselemente aus der Ausgabe entfernen | False |
| `-c, --clean` | Skripte, Stile und Metatags entfernen | False |
| `-fil, --filter` | Regex-Muster zum Filtern von Seiten nach Titel oder URL | None |
| `-m, --max-pages` | Maximale Anzahl von Seiten, die gecrawlt werden sollen | None |
| `-v, --verbose` | Detaillierte Debug-Informationen anzeigen | False |

## 📁 Ausgabestruktur

Der Crawler erstellt die folgende Struktur in deinem Ausgabeverzeichnis:

```
output_directory/
├── index.json          # JSON-Index aller gecrawlten Seiten
├── README.md           # Übersicht für Menschen
├── 00_Introduction.md  # Nummerierte Inhaltsdateien
├── 01_Chapter_One.md
├── 02_Chapter_Two.md
└── ...
```

### Dateibenennungskonvention

- Dateien sind mit dynamischer Pufferung nummeriert (z. B. `01_`, `001_`, `0001_`)
- Kapitelnumerierungen werden aus der Quelle beibehalten
- Unnummerierte Seiten erhalten eine Null-Pufferung (z. B. `00_`, `000_`)
- Sonderzeichen werden aus Dateinamen entfernt
- Dateinamen werden auf 40 Zeichen gekürzt

### Indexdateien

**index.json**: Maschinenlesbarer Index
```json
{
  "format": "md",
  "total_chapters": 15,
  "files": [
    {
      "filename": "01_Introduction.md",
      "url": "https://example.com/intro.html",
      "chapter_number": "1",
      "title": "Introduction",
      "index": 0
    }
  ]
}
```

**README.md**: Übersicht für Menschen mit einer Tabelle aller gecrawlten Seiten

## 🏆 Best Practices

### 1. **Verwende immer Verzögerungen für große Seiten**
```bash
scrwl -u https://example.com -o ./output -f md -d 1.0
```
Dies verhindert, dass der Server überlastet wird, und verringert die Wahrscheinlichkeit, dass du eine Ratenbegrenzung erhältst.

### 2. **Beginne mit einem Trockenlauf**
```bash
scrwl -u https://example.com -o ./output -f md -n
```
Vorschau darauf, was gecrawlt wird, bevor du dich für einen vollständigen Crawl entscheidest.

### 3. **Verwende die bereinigte Ausgabe zum Lesen**
```bash
scrwl -u https://example.com -o ./output -f md -c -N
```
Entfernt unnötige Elemente für ein saubereres Leseerlebnis.

### 4. **Setze unterbrochene Crawls fort**
```bash
scrwl -u https://example.com -o ./output -f md -s
```
Die `-s`-Option überspringt vorhandene Dateien, perfekt zum Fortsetzen.

### 5. **Filtere nach bestimmten Inhalten**
```bash
scrwl -u https://docs.example.com -o ./output -f md -fil "api|reference"
```
Crawle nur Seiten, die deinem Muster entsprechen.

### 6. **Setze angemessene Timeouts**
```bash
scrwl -u https://slow-site.com -o ./output -f md -t 60
```
Erhöhe das Timeout für langsame Seiten.

## 🔍 So funktioniert's

1. **Navigationsanalyse**: Der Crawler analysiert zuerst die Startseite, um alle Navigationslinks zu extrahieren
2. **Reihenfolgenbestimmung**: Er erkennt intelligent die Kapitelnumerierungen und sortiert die Seiten entsprechend
3. **Intelligentes Crawlen**: Seiten werden in der richtigen Reihenfolge mit konfigurierbaren Verzögerungen gecrawlt
4. **Linkkorrektur**: Interne Links werden automatisch aktualisiert, um mit den neuen Dateinamen übereinzustimmen
5. **Indexerstellung**: Erstellt sowohl JSON- als auch Markdown-Indexes für eine einfache Navigation

## 🐛 Fehlerbehebung

### Häufige Probleme

**Ratenbegrenzung**
- Lösung: Erhöhe die Verzögerung mit `-d 2.0` oder höher

**Timeout-Fehler**
- Lösung: Erhöhe das Timeout mit `-t 60`

**Speicherprobleme bei großen Seiten**
- Lösung: Verwende `-m 100`, um die Seiten pro Durchlauf zu begrenzen

**Kodierungsfehler**
- Der Crawler verarbeitet standardmäßig UTF-8
- Sonderzeichen werden im Inhalt beibehalten

### Debug-Modus

Verwende `-v` für ausführliche Ausgaben zur Diagnose von Problemen:
```bash
scrwl -u https://example.com -o ./output -f md -v
```

## 🤝 Mitwirken

Beiträge sind willkommen! Bitte zögere nicht, einen Pull Request einzureichen. Bei größeren Änderungen öffne bitte zuerst ein Issue, um zu besprechen, was du ändern möchtest.

### Entwicklungseinrichtung

```bash
# Repo klonen
git clone https://github.com/marifl/marifl_crawling.git
cd marifl_crawling

# Im Entwicklungsmodus installieren
uv sync

# Tests ausführen (wenn verfügbar)
pytest
```

## 📄 Lizenz

Dieses Projekt ist lizenziert unter der MIT-Lizenz - siehe die [LICENSE](LICENSE)-Datei für Details.

## 🙏 Danksagungen

- Basierend auf [crawl4ai](https://github.com/unclecode/crawl4ai) für robustes Web-Crawling
- Verwendet [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) zur HTML-Analyse
- [html2text](https://github.com/Alir3z4/html2text/) zur Markdown-Konvertierung

## 📮 Unterstützung

Wenn du auf Probleme stößt oder Fragen hast:

1. Überprüfe den Abschnitt [Fehlerbehebung](#-fehlerbehebung)
2. Suche nach [bestehenden Problemen](https://github.com/marifl/marifl_crawling/issues)
3. Erstelle ein neues Issue mit:
   - Deinem Befehl
   - Fehlermeldung
   - Python-Version
   - Betriebssystem

---

Hergestellt mit ❤️ von marifl in Zusammenarbeit mit GitHub Copilot

---

Mancherorts kann crawling nicht erlaubt sein. Prüfe das vorher. Jeder ist für sich selbst verantwortlich, also übernimmm die Verantwortung für dein eigenes Handeln! - alles ist "as is" kein gewähr für irgendwas, Nutzung auf eigene Gefahr usw.....