# 🤝 Beitragen zu marifl_crawling

Vielen Dank für Ihr Interesse, zu diesem Projekt beizutragen! Als Einzelentwickler freue ich mich über jede Hilfe.

## 📋 Wie Sie beitragen können

### 🐛 Fehler melden

Wenn Sie einen Fehler finden:

1. **Prüfen Sie die bestehenden Issues**, um sicherzustellen, dass der Fehler noch nicht gemeldet wurde
2. **Öffnen Sie ein neues Issue** mit folgenden Informationen:
   - Detaillierte Beschreibung des Problems
   - Schritte zur Reproduktion
   - Erwartetes vs. tatsächliches Verhalten
   - Ihre Systemumgebung (OS, Python-Version, uv-Version)
   - Relevante Logs oder Fehlermeldungen

### 💡 Feature-Vorschläge

Für neue Funktionen:

1. **Öffnen Sie ein Issue** mit dem Label "enhancement"
2. **Beschreiben Sie** das gewünschte Feature detailliert
3. **Erklären Sie den Anwendungsfall** und warum es nützlich wäre
4. **Diskutieren Sie** mit den Maintainern über die Implementierung

### 🔧 Code-Beiträge

#### Entwicklungsumgebung einrichten

```bash
# Repository forken und klonen
git clone https://github.com/IHRBENUTZERNAME/marifl_crawling.git
cd marifl_crawling

# Entwicklungsumgebung einrichten
uv sync
uv run crawl4ai-setup

# Neue Branch für Ihr Feature erstellen
git checkout -b feature/ihr-feature-name
```

#### Coding-Standards

- **Python-Stil**: Befolgen Sie PEP 8
- **Docstrings**: Verwenden Sie deutsche Kommentare und Docstrings
- **Funktionsnamen**: Verwenden Sie aussagekräftige, deutsche Namen
- **Kommentare**: Schreiben Sie klare, deutsche Kommentare

**Beispiel:**
```python
def extrahiere_kapitel_titel(self, url: str) -> str:
    """
    Extrahiert den Kapiteltitel aus einer Bookdown-Seite.
    
    Args:
        url: Die URL der zu analysierenden Seite
        
    Returns:
        Der bereinigte Kapiteltitel
        
    Raises:
        RequestException: Wenn die Seite nicht erreichbar ist
    """
    # Implementation hier...
```

#### Testing

```bash
# Tests ausführen (falls vorhanden)
uv run pytest

# Ihr Code testen
uv run scrwl --help
uv run scrwl -u https://example.com -o ./test -f md -n  # Dry run
```

#### Pull Request einreichen

1. **Stellen Sie sicher**, dass Ihr Code funktioniert
2. **Commiten Sie** Ihre Änderungen mit aussagekräftigen Commit-Nachrichten:
   ```bash
   git commit -m "Füge Unterstützung für neue Bookdown-Versionen hinzu"
   ```
3. **Pushen Sie** Ihre Branch:
   ```bash
   git push origin feature/ihr-feature-name
   ```
4. **Öffnen Sie einen Pull Request** mit:
   - Klarer Beschreibung der Änderungen
   - Bezug auf relevante Issues
   - Screenshots oder Beispiele, falls anwendbar

## 📝 Commit-Konventionen

Verwenden Sie klare, deutsche Commit-Nachrichten:

- `Füge [Feature] hinzu` - für neue Funktionen
- `Behebt [Problem]` - für Fehlerbehebungen
- `Aktualisiert [Komponente]` - für Updates
- `Entfernt [Feature]` - für entfernte Funktionen
- `Dokumentiert [Bereich]` - für Dokumentationsänderungen

**Beispiele:**
```bash
git commit -m "Füge Unterstützung für PDF-Export hinzu"
git commit -m "Behebt Problem mit Unicode-Zeichen in Dateinamen"
git commit -m "Aktualisiert README mit neuen Installationsanweisungen"
```

## 🎯 Entwicklungsprioritäten

Besonders willkommen sind Beiträge in diesen Bereichen:

### Hoch prioritär:
- **Fehlerbehandlung** verbessern
- **Performance-Optimierungen** für große Sites
- **Unterstützung für mehr Website-Typen** (über Bookdown hinaus)
- **Bessere Link-Erkennung** und -Konvertierung

### Mittel prioritär:
- **Export-Optionen** (PDF, EPUB)
- **GUI-Interface** für weniger technische Nutzer
- **Konfigurations-Dateien** für komplexe Setups
- **Plugin-System** für Erweiterungen

### Niedrig prioritär:
- **Themes** für HTML-Output
- **Statistiken** über gecrawlte Inhalte
- **Integration** mit anderen Tools

## 🚫 Was wir NICHT akzeptieren

- Code ohne ausreichende Dokumentation
- Breaking Changes ohne vorherige Diskussion
- Features, die die Einfachheit des Tools stark beeinträchtigen
- Code, der ethische oder rechtliche Bedenken aufwirft

## 📞 Fragen oder Hilfe?

- **GitHub Issues**: Für Bugs und Feature-Requests
- **Diskussionen**: Für allgemeine Fragen und Ideen
- **E-Mail**: Für private oder sicherheitsrelevante Anfragen

## 🙏 Anerkennung

Alle Beitragenden werden in der [Contributors](https://github.com/marifl/marifl_crawling/graphs/contributors) Liste aufgeführt.

Bedeutende Beiträge werden auch im README erwähnt.

---

**Wichtig**: Durch das Beitragen zu diesem Projekt stimmen Sie zu, dass Ihre Beiträge unter der MIT-Lizenz lizenziert werden, die auch für den Rest des Projekts gilt.
