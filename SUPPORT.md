# 🆘 Support & Hilfe

Benötigen Sie Hilfe mit `marifl_crawling`? Hier finden Sie verschiedene Wege, um Unterstützung zu erhalten.

## 🚀 Schnelle Hilfe

### 📖 Dokumentation
Bevor Sie um Hilfe bitten, schauen Sie bitte in unsere ausführliche Dokumentation:

- **[README.md](README.md)** - Vollständige Projektübersicht und Anleitung
- **[INSTRUCTIONS.md](INSTRUCTIONS.md)** - Schritt-für-Schritt Tutorials
- **Inline-Hilfe**: `scrwl --help` für alle verfügbaren Optionen

### 🔧 Häufige Probleme lösen

#### "Browser executable not found"
```bash
# Lösung: Setup ausführen
uv run crawl4ai-setup
```

#### "Command not found: scrwl"
```bash
# Lösung 1: Als globales Tool installieren
uv tool install .

# Lösung 2: Mit uv run verwenden
uv run scrwl -u URL -o DIR -f md
```

#### Rate Limiting / Zu viele Anfragen
```bash
# Lösung: Verzögerung erhöhen
scrwl -u URL -o DIR -f md -d 3.0
```

#### Timeout-Fehler
```bash
# Lösung: Timeout erhöhen
scrwl -u URL -o DIR -f md -t 60
```

## 📞 Support-Kanäle

### 1. 🐛 GitHub Issues (Empfohlen)
**Für**: Bugs, Feature-Requests, technische Probleme

**Link**: [GitHub Issues](https://github.com/marifl/marifl_crawling/issues)

**Bevor Sie ein Issue erstellen:**
- [ ] Prüfen Sie, ob das Problem bereits gemeldet wurde
- [ ] Lesen Sie die Dokumentation
- [ ] Versuchen Sie die häufigen Lösungen oben

**Für Ihr Issue, bitte angeben:**
```
Problem-Beschreibung:
[Detaillierte Beschreibung des Problems]

Schritte zur Reproduktion:
1. [Schritt 1]
2. [Schritt 2] 
3. [Schritt 3]

Erwartetes Verhalten:
[Was sollte passieren]

Tatsächliches Verhalten:
[Was passiert tatsächlich]

Umgebung:
- Betriebssystem: [z.B. macOS 14.5]
- Python-Version: [z.B. 3.11.6]
- UV-Version: [z.B. 0.1.32]
- marifl_crawling Version: [z.B. 1.0.0]

Verwendeter Befehl:
[Der exakte scrwl-Befehl, den Sie verwendet haben]

Fehlermeldung:
[Falls vorhanden, die komplette Fehlermeldung]
```

### 2. 💬 GitHub Discussions
**Für**: Allgemeine Fragen, Verwendungsbeispiele, Community-Austausch

**Link**: [GitHub Discussions](https://github.com/marifl/marifl_crawling/discussions)

**Ideal für:**
- "Wie crawle ich Website X?"
- "Welche Optionen sind für Y am besten?"
- "Erfahrungsaustausch mit anderen Nutzern"
- "Feature-Ideen diskutieren"

### 3. ✉️ E-Mail Support
**Für**: Private Anfragen, Geschäftliches, Sicherheitsprobleme

**E-Mail**: [support@marifl.example.com] *(Bitte durch tatsächliche Support-E-Mail ersetzen)*

**Bearbeitungszeit**: 1-3 Werktage

**Bitte verwenden Sie E-Mail nur für:**
- Private oder sensible Anfragen
- Geschäftliche Partnerschaften
- Sicherheitsprobleme (siehe [SECURITY.md](SECURITY.md))

## 📚 Selbsthilfe-Ressourcen

### 🎯 Tutorials & Guides
- **[INSTRUCTIONS.md](INSTRUCTIONS.md)** - Detaillierte Schritt-für-Schritt Anleitung
- **README.md** - Umfassende Dokumentation mit Beispielen
- **Code-Kommentare** - Der Code ist ausführlich dokumentiert

### 🔍 Debugging
```bash
# Verbose-Modus für detaillierte Ausgaben
scrwl -u URL -o DIR -f md -v

# Dry-run um zu sehen, was passieren würde
scrwl -u URL -o DIR -f md -n

# Mit erhöhtem Timeout und Delay testen
scrwl -u URL -o DIR -f md -t 60 -d 2.0
```

### 📊 Logs analysieren
Das Tool gibt detaillierte Statusmeldungen aus:
- ✅ **Grüne Checkmarks**: Erfolgreiche Operationen
- ❌ **Rote X**: Fehler oder Probleme
- ⚠️ **Gelbe Warnungen**: Hinweise oder Warnungen
- 🔄 **Blaue Pfeile**: Wiederholungsversuche

## 🏷️ Issue-Labels verstehen

Wenn Sie ein Issue erstellen, werden diese Labels verwendet:

- **🐛 bug**: Bestätigter Fehler
- **✨ enhancement**: Neue Feature-Anfrage  
- **📖 documentation**: Verbesserungen der Dokumentation
- **❓ question**: Frage zur Nutzung
- **🆘 help wanted**: Wir suchen Community-Hilfe
- **🔴 priority-high**: Kritische Probleme
- **🟡 priority-medium**: Wichtige Probleme
- **🟢 priority-low**: Niedrige Priorität
- **🚫 wontfix**: Wird nicht behoben

## ⏰ Response-Zeiten

**GitHub Issues/Discussions:**
- **Erste Antwort**: 1-3 Tage
- **Bugfixes**: 1-2 Wochen (je nach Komplexität)
- **Features**: 2-4 Wochen (nach Diskussion)

**E-Mail:**
- **Erste Antwort**: 1-3 Werktage
- **Detaillierte Antwort**: 3-7 Werktage

## 🤝 Community Support

### Gegenseitige Hilfe
Unsere Community ist sehr hilfsbereit! Andere Nutzer können oft schnell helfen bei:
- Spezifischen Website-Problemen
- Konfigurationsfragen
- Verwendungsbeispielen

### Selbst helfen
Sie können auch anderen helfen:
- Beantworten Sie Fragen in Issues/Discussions
- Teilen Sie Ihre Erfahrungen und Lösungen
- Verbessern Sie die Dokumentation

## 🚫 Was wir NICHT supporten

- **Illegale Aktivitäten**: Crawling ohne Erlaubnis, Urheberrechtsverletzungen
- **Kommerzielle Website-Analysen**: Ohne entsprechende Vereinbarung
- **Reverse Engineering**: Von geschützten Websites oder APIs
- **Spam oder Missbrauch**: Des Tools für schädliche Zwecke

## 💡 Support-Tipps

### Gute Fragen stellen:
1. **Seien Sie spezifisch**: "Funktioniert nicht" vs. "Fehler 404 bei r4ds.had.co.nz"
2. **Geben Sie Kontext**: Welche URL? Welche Optionen? Welches System?
3. **Zeigen Sie, was Sie versucht haben**: Welche Lösungen haben Sie probiert?
4. **Fügen Sie relevante Informationen hinzu**: Logs, Screenshots, Befehle

### Bessere Antworten erhalten:
- **Verwenden Sie GitHub Issues** für technische Probleme
- **Markieren Sie dringende Probleme** entsprechend
- **Folgen Sie den Templates** wenn vorhanden
- **Seien Sie geduldig** - wir sind hauptsächlich freiwillige Entwickler

## 🎉 Erfolgsstories teilen

Haben Sie `marifl_crawling` erfolgreich für ein interessantes Projekt verwendet? Wir freuen uns über:
- **Screenshots** Ihrer gecrawlten Bücher
- **Use-Case-Beschreibungen** in Discussions
- **Verbesserungsvorschläge** basierend auf Ihren Erfahrungen

---

**Danke, dass Sie marifl_crawling verwenden!** 

Ihr Feedback hilft uns, das Tool für alle zu verbessern. 🚀
