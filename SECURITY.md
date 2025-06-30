# 🔒 Sicherheitsrichtlinie

## 🚨 Meldung von Sicherheitslücken

Die Sicherheit von `marifl_crawling` ist uns sehr wichtig. Wenn Sie eine Sicherheitslücke in diesem Projekt entdecken, bitten wir Sie, uns diese verantwortungsvoll zu melden.

### ⚡ Schnellmeldung

**Für kritische Sicherheitslücken:**
- **E-Mail**: [security@marifl.example.com] *(Bitte durch tatsächliche Sicherheits-E-Mail ersetzen)*
- **Betreff**: `[SECURITY] marifl_crawling - [Kurze Beschreibung]`

### 📋 Was zu melden ist

Melden Sie bitte Sicherheitslücken, die folgende Bereiche betreffen könnten:

#### 🔴 Hoch kritisch:
- **Code-Injection** durch bösartige Website-Inhalte
- **Path-Traversal** Angriffe beim Dateischreiben
- **Remote Code Execution** durch unsichere Deserialisierung
- **Privilege Escalation** im lokalen System

#### 🟡 Mittel kritisch:
- **Information Disclosure** durch Log-Dateien
- **DoS-Angriffe** durch Speicher-/CPU-Erschöpfung
- **Unsichere Standardkonfigurationen**
- **Dependency-Vulnerabilities** in verwendeten Bibliotheken

#### 🟢 Niedrig kritisch:
- **Minor Information Leaks**
- **Usability-bezogene Sicherheitsprobleme**

### 📝 Informationen für Ihren Bericht

Bitte fügen Sie folgende Informationen in Ihren Sicherheitsbericht ein:

```
Schweregrad: [Hoch/Mittel/Niedrig]
Komponente: [z.B. smart_crawler_final.py, Zeile X]
Beschreibung: [Detaillierte Beschreibung der Schwachstelle]

Reproduktion:
1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]

Erwartetes Verhalten:
[Was sollte passieren]

Tatsächliches Verhalten:
[Was passiert tatsächlich]

Auswirkungen:
[Potentielle Schäden oder Risiken]

Umgebung:
- Betriebssystem: [z.B. macOS 14.5]
- Python-Version: [z.B. 3.11.6]
- UV-Version: [z.B. 0.1.32]
- marifl_crawling Version: [z.B. 1.0.0]

Proof of Concept:
[Falls vorhanden, fügen Sie einen sicheren PoC hinzu]
```

### ⏰ Response-Zeiten

Wir streben folgende Antwortzeiten an:

- **Bestätigung des Eingangs**: Innerhalb von 24 Stunden
- **Erste Bewertung**: Innerhalb von 72 Stunden
- **Status-Update**: Wöchentlich bis zur Lösung
- **Fix-Release**: Je nach Schweregrad 7-30 Tage

### 🔄 Unser Prozess

1. **Eingang**: Wir bestätigen den Erhalt Ihres Berichts
2. **Bewertung**: Wir bewerten Schweregrad und Auswirkungen
3. **Entwicklung**: Wir entwickeln und testen einen Fix
4. **Koordination**: Wir koordinieren die Veröffentlichung mit Ihnen
5. **Release**: Wir veröffentlichen den Fix
6. **Anerkennung**: Wir würdigen Ihren Beitrag (falls gewünscht)

### 🎯 Verantwortliche Offenlegung

Wir folgen dem Prinzip der **responsible disclosure**:

#### ✅ Bitte TUN Sie:
- Geben Sie uns angemessene Zeit, das Problem zu beheben
- Vermeiden Sie den Zugriff auf fremde Daten
- Demonstrieren Sie die Schwachstelle nur minimal
- Informieren Sie uns über alle betroffenen Versionen

#### ❌ Bitte tun Sie NICHT:
- Die Schwachstelle öffentlich preisgeben, bevor ein Fix verfügbar ist
- Produktive Systeme angreifen oder schädigen
- Daten stehlen, ändern oder löschen
- Social Engineering gegen Projektmitglieder betreiben

### 🏆 Anerkennung

Wir sind dankbar für verantwortungsvolle Sicherheitsforscher und möchten angemessene Anerkennung bieten:

#### 🎖️ Hall of Fame
Berichterstatter werden (mit ihrer Erlaubnis) in unserer Sicherheits-Hall-of-Fame erwähnt:

- **[Ihr Name]** - [Datum] - [Art der Schwachstelle]

#### 📜 Credits
- Erwähnung in Release Notes
- LinkedIn-Empfehlung (falls gewünscht)
- Referenz für zukünftige Sicherheitsarbeiten

### 🛡️ Unterstützte Versionen

Wir unterstützen Sicherheitsupdates für folgende Versionen:

| Version | Unterstützt          |
| ------- | -------------------- |
| 1.0.x   | ✅ Vollständig       |
| < 1.0   | ❌ Nicht unterstützt |

### 🔧 Selbstverteidigung

Um die Sicherheit bei der Nutzung von `marifl_crawling` zu maximieren:

#### ✅ Empfohlene Sicherheitsmaßnahmen:
- **Führen Sie das Tool nicht als root/Administrator aus**
- **Verwenden Sie einen separaten Ordner für Downloads**
- **Prüfen Sie URLs vor dem Crawling auf Vertrauenswürdigkeit**
- **Begrenzen Sie die Anzahl gecrawlter Seiten bei unbekannten Sites**
- **Verwenden Sie aktuelle Versionen** aller Dependencies

#### ⚠️ Bekannte Einschränkungen:
- Das Tool lädt und führt JavaScript aus (via crawl4ai)
- Heruntergeladene Inhalte können bösartigen Code enthalten
- Keine Sandbox-Isolation zwischen gecrawlten Sites

### 📚 Zusätzliche Ressourcen

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Common Vulnerability Scoring System (CVSS)](https://www.first.org/cvss/)
- [Responsible Disclosure Guidelines](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)

### 📞 Kontakt

Für nicht-sicherheitsrelevante Fragen:
- **GitHub Issues**: Für Bugs und Features
- **E-Mail**: [info@marifl.example.com] *(Bitte durch tatsächliche Kontakt-E-Mail ersetzen)*

---

**Letzte Aktualisierung**: 30. Juni 2025

**Danke** für Ihren Beitrag zur Sicherheit von marifl_crawling! 🙏
