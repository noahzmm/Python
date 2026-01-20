# Vigenère-Cipher Tool

Ein interaktives Python-Programm zur Ver- und Entschlüsselung von Texten mit der Vigenère-Verschlüsselung, inklusive Kryptoanalyse-Funktionen.

## Beschreibung

Die Vigenère-Verschlüsselung ist ein historisches Verschlüsselungsverfahren, das auf einer polyalphabetischen Substitution basiert. Im Gegensatz zur einfachen Caesar-Verschlüsselung wird hier jeder Buchstabe mit einem anderen Verschiebungswert verschlüsselt, basierend auf einem Schlüsselwort.

## Funktionen

### 1. 🔒 Verschlüsseln
Verschlüsselt einen beliebigen Text mit einem Schlüsselwort:
- Eingabe: Klartext und Schlüssel
- Ausgabe: Verschlüsselter Text (Ciphertext)
- Sonderzeichen und Leerzeichen bleiben erhalten

### 2. 🔓 Entschlüsseln
Entschlüsselt einen verschlüsselten Text mit dem bekannten Schlüssel:
- Eingabe: Ciphertext und Schlüssel
- Ausgabe: Originaltext (Klartext)

### 3. 📊 Häufigkeitsanalyse
Manuelle Kryptoanalyse durch Buchstabenhäufigkeitsanalyse:
- Zeigt die häufigsten Buchstaben im verschlüsselten Text
- Vergleich mit typischen deutschen Buchstabenhäufigkeiten (E, N, I, S, R)
- Manuelle Ersetzung einzelner Buchstaben zur schrittweisen Entschlüsselung
- Befehle:
  - `X=Y`: Ersetzt alle Vorkommen von X durch Y
  - `reset`: Setzt den Text auf das Original zurück
  - `exit`: Beendet die Analyse

### 4. 💥 Brute-Force-Angriff
Automatisches Testen aller möglichen Schlüssel:
- Eingabe: Verschlüsselter Text, erwartetes Wort, Schlüssellänge
- Probiert systematisch alle Schlüsselkombinationen durch
- Stoppt, wenn das erwartete Wort im entschlüsselten Text gefunden wird
- Zeigt Statistiken: gefundener Schlüssel, benötigte Zeit, Anzahl der Versuche

⚠️ **Warnung**: Die Anzahl möglicher Schlüssel wächst exponentiell (26^n für Länge n)!
- Länge 2: 676 Kombinationen
- Länge 3: 17.576 Kombinationen
- Länge 4: 456.976 Kombinationen
- Länge 5: 11.881.376 Kombinationen

## Installation

### Voraussetzungen
- Python 3.10 oder höher (wegen `match`-Statement)
- Keine externen Bibliotheken erforderlich (nur Python-Standardbibliothek)

### Setup
```bash
# Repository klonen oder herunterladen
git clone <repository-url>
cd Vigenere

# Programm ausführen
python Vigenere.py
```

## Verwendung

### Beispiel: Verschlüsseln
```
Auswahl: 1
Text: HELLO WORLD
Schlüssel: KEY
Ergebnis: RIJVS UYVJN
```

### Beispiel: Entschlüsseln
```
Auswahl: 2
Text: RIJVS UYVJN
Schlüssel: KEY
Ergebnis: HELLO WORLD
```

### Beispiel: Brute-Force
```
Auswahl: 4
Text: RIJVS
Erwartetes Wort: HELLO
Schlüssellänge: 3
Ergebnis: Schlüssel gefunden: KEY
```

## Technische Details

### Funktionsweise
1. **Verschlüsselung**: Jeder Buchstabe wird um den Wert des entsprechenden Schlüsselbuchstabens im Alphabet verschoben
2. **Schlüsselwiederholung**: Der Schlüssel wird zyklisch wiederholt, falls der Text länger ist
3. **Modulo-Arithmetik**: Überschreitungen über 'Z' hinaus werden durch Modulo 26 behandelt

### Formel
- Verschlüsselung: `C[i] = (P[i] + K[i mod len(K)]) mod 26`
- Entschlüsselung: `P[i] = (C[i] - K[i mod len(K)]) mod 26`

Wobei:
- P = Plaintext (Klartext)
- C = Ciphertext (Verschlüsselter Text)
- K = Key (Schlüssel)

## Verwendete Module
- `collections`: Für Buchstabenhäufigkeitszählung (Counter)
- `time`: Für Zeitmessung beim Brute-Force-Angriff
- `itertools`: Für Generierung aller Schlüsselkombinationen
- `os` & `platform`: Für plattformunabhängige Konsolenlöschung

## Sicherheitshinweise

Die Vigenère-Verschlüsselung gilt heute als **nicht sicher** und sollte **nicht für echte Geheimnisse** verwendet werden!

**Schwächen**:
- Anfällig für Häufigkeitsanalyse bei kurzen Schlüsseln
- Kasiski-Test kann Schlüssellänge ermitteln
- Moderne Computer können kurze Schlüssel in Sekunden knacken

**Empfehlung**: Für echte Sicherheit moderne Verschlüsselungsverfahren wie AES verwenden.

## Lizenz

Dieses Projekt ist zu Bildungszwecken erstellt worden.

## Autor

Entwickelt als Lernprojekt zur Demonstration klassischer Kryptographie.

## Weiterführende Informationen

- [Wikipedia: Vigenère-Verschlüsselung](https://de.wikipedia.org/wiki/Vigen%C3%A8re-Verschl%C3%BCsselung)
- [Kasiski-Test](https://de.wikipedia.org/wiki/Kasiski-Test)
- [Buchstabenhäufigkeit im Deutschen](https://de.wikipedia.org/wiki/Buchstabenh%C3%A4ufigkeit)
