"""
Vigenère-Cipher Tool
====================
Ein interaktives Programm zur Ver- und Entschlüsselung von Texten 
mit der Vigenère-Verschlüsselung.

Funktionen:
1. Verschlüsseln - Text mit einem Schlüssel verschlüsseln
2. Entschlüsseln - Text mit bekanntem Schlüssel entschlüsseln
3. Häufigkeitsanalyse - Manuelle Kryptoanalyse durch Buchstabenersetzung
4. Brute-Force-Angriff - Automatisches Testen aller möglichen Schlüssel
"""

import collections
import time
import itertools
import os
import platform


def clear_console():
    """
    Löscht die Konsolenausgabe plattformunabhängig.
    
    Verwendet 'cls' für Windows und 'clear' für Unix-basierte Systeme.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


clear_console()

# Alphabet für die Vigenère-Verschlüsselung (nur Großbuchstaben)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Benutzerauswahl des gewünschten Modus
selection = int(input("1. Verschlüsseln \n2. Entschlüsseln\n3. Häufigkeitsanalyse\n4. Brute-Force Attack\nEingabe: "))
clear_console()

match selection: 
    case 1:  # Verschlüsselung
        """
        Verschlüsselt einen Text mit dem Vigenère-Verfahren.
        Der Benutzer gibt Text und Schlüssel ein.
        """
        text = input("Zu verschlüsselnden Text angeben: ").upper()
        clear_console()
        key = input("Schlüssel angeben zum verschlüsseln: ").upper()
        clear_console()
        res = ""
        key_index = 0
        
        # Jeden Buchstaben des Textes verschlüsseln
        for char in text:
            if char in alphabet:
                # Shift-Wert aus dem Schlüssel ermitteln
                shift = alphabet.find(key[key_index % len(key)])
                # Caesar-Verschiebung mit dem Shift-Wert durchführen
                res += alphabet[(alphabet.find(char) + shift) % 26]
                key_index += 1 
            else:
                # Sonderzeichen und Leerzeichen unverändert übernehmen
                res += char 

        print("Verschlüsselter Text: \n" + res)

    case 2:  # Entschlüsselung
        """
        Entschlüsselt einen mit Vigenère verschlüsselten Text.
        Der Benutzer muss den korrekten Schlüssel kennen.
        """
        text = input("Zu entschlüsselnden Text angeben: ").upper()
        clear_console()
        key = input("Schlüssel angeben zum entschlüsseln: ").upper()
        clear_console()
        res = ""
        key_index = 0

        # Jeden Buchstaben des verschlüsselten Textes entschlüsseln
        for char in text:
            if char in alphabet:
                # Shift-Wert aus dem Schlüssel ermitteln
                shift = alphabet.find(key[key_index % len(key)])
                # Rückwärts-Verschiebung durchführen
                res += alphabet[(alphabet.find(char) - shift) % 26]
                key_index += 1
            else:
                # Sonderzeichen und Leerzeichen unverändert übernehmen
                res += char
            
        print("Entschlüsselter Text : \n" + res)

    case 3:  # Häufigkeitsanalyse
        """
        Manuelle Kryptoanalyse durch Häufigkeitsanalyse.
        Zeigt die häufigsten Buchstaben und erlaubt manuelle Ersetzungen.
        """
        ciphertext = input("Verschlüsselten Text angeben: ").upper()
        current_text = ciphertext
        
        while True:
            clear_console()
            print("--- Manuelle Ersetzung (Häufigkeitsanalyse) ---")
            print(f"\nAktueller Text:\n{current_text}")
            print("-" * 40)
            
            # Buchstabenhäufigkeit berechnen
            filtered = [c for c in current_text if c in alphabet]
            counts = collections.Counter(filtered).most_common(5)
            
            # Top 5 Buchstaben anzeigen
            print("Top 5 Buchstaben im Text:")
            for char, count in counts:
                perc = (count / len(filtered)) * 100 if filtered else 0
                print(f"'{char}': {perc:.1f}%")
            
            print("\nHinweis: Deutsch häufigste: E, N, I, S, R")
            print("-" * 40)
            print("Befehle: 'X=Y' (ersetze X durch Y), 'reset' (Original), 'exit' (Ende)")
            
            action = input("Eingabe: ").upper()
            
            if action == 'EXIT':
                break
            elif action == 'RESET':
                current_text = ciphertext
                continue
            elif "=" in action:
                try:
                    # Buchstabenersetzung durchführen
                    old_char, new_char = action.split("=")
                    current_text = current_text.replace(old_char.strip(), new_char.strip().lower())
                except:
                    print("Fehler! Format: A=E")
                    time.sleep(1)
            else:
                print("Ungültige Eingabe.")
                time.sleep(1)

        print(f"\nFinaler Text:\n{current_text.upper()}")

    case 4:  # Brute-Force-Angriff
        """
        Brute-Force-Angriff auf Vigenère-Verschlüsselung.
        Probiert alle möglichen Schlüssel einer bestimmten Länge durch,
        bis ein erwartetes Wort im entschlüsselten Text gefunden wird.
        
        Warnung: Die Anzahl möglicher Schlüssel steigt exponentiell mit der Länge!
        Für Länge n gibt es 26^n Möglichkeiten.
        """
        ciphertext = input("Verschlüsselten Text eingeben: ").upper()
        clear_console()
        expected_word = input("Welches Wort wird im Text vermutet (zum Stoppen)? ").upper()
        clear_console()
        length = int(input("Für Schlüssellänge testen: "))
        clear_console()

        start_time = time.time()
        attempts = 0
        found = False

        print("Starte Angriff... Bitte warten.")
        
        # Alle möglichen Schlüsselkombinationen durchprobieren
        for p in itertools.product(alphabet, repeat=length):
            attempts += 1
            current_key = "".join(p)
            res = ""
            key_index = 0

            # Text mit aktuellem Schlüssel entschlüsseln
            for char in ciphertext:
                if char in alphabet:
                    shift = alphabet.find(current_key[key_index % len(current_key)])
                    res += alphabet[(alphabet.find(char) - shift) % 26]
                    key_index += 1
                else:
                    res += char
                
            # Prüfen, ob das erwartete Wort im entschlüsselten Text vorkommt
            if expected_word in res:
                end_time = time.time()
                duration = end_time - start_time
                clear_console()    
                print(f"Schlüssel gefunden: {current_key}")
                print(f"Text: {res[:50]}...")
                print(f"Benötigte Zeit: {duration:.4f} Sekunden")
                print(f"Geprüfte Schlüssel: {attempts}")
                found = True
                break
        
        # Falls kein passender Schlüssel gefunden wurde
        if not found:
            end_time = time.time()
            duration = end_time - start_time
            clear_console()
            print(f"Nichts gefunden nach {attempts} Versuchen.")
            print(f"Dauer: {duration:.4f} Sekunden")

    case _:  # Ungültige Eingabe
        print("Ungültige Auswahl")