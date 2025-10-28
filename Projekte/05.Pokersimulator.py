import random
# liste 52 Zahlen
# floor divison
# modulo 13 um aufs symbol zu kommen
# 5 int alle Farben ausrechen (durch 13)
# Symbole modulo 13
# set auf 5 karten dann sind sie von gleicher farbe
# paar for Schleife äußere von 0-vorletzte
# drillinge counter
# straße aufsteigend
# flush + straße = royal flush
# unwahrscheinlichste zuerst wahrscheinlichste zuletzt
# Straße übers Eck dabei oder nicht ausprobieren


def karten_Zuteilen():
    erg = [i for i in range(1, 53)]
    return erg


def ziehung(vorkommen):
    zahl = list(range(1, 53))
    erg = []
    for j in range(5):
        gezogen = random.randint(0, len(zahl) - j - 1)
        gezogene_zahl = zahl[gezogen]
        erg.append(gezogen)
        letzte_position = len(zahl) - j - 1
        letzte_zahl = zahl[letzte_position]
        zahl[gezogen] = letzte_zahl
        zahl[letzte_position] = gezogene_zahl
    return erg

def kartenwerte(gezogene):
    """
    Rechnet die gezogenen Karten (1–52) in Werte von 1–13 um.
    Dabei ist:
    1 = Ass, 11 = Bube, 12 = Dame, 13 = König
    """
    werte = [(karte - 1) % 13 + 1 for karte in gezogene]
    return werte


def flush(gezogene):
    gedreht = gezogene[:]   ### erstellt eine Kopie, damit nicht so viel Speicher verwendet wird! Noch googlen!
    gedreht.reverse()
    for i in range(1, len(gedreht)):
        if not ((gedreht[i] - 1) // 13 == (gedreht[i - 1] - 1) // 13):
            ### floor devision noch vorher -1, weil KI-Hilfe!
            return False
    return True

'''
            Kartennummer
            Ohne -1
            Mit -1 (korrekt)
            1 (Herz Ass)
            1 // 13 = 0 ✓
            (1-1) // 13 = 0 ✓
            13 (Herz König)
            13 // 13 = **1** ❌
            (13-1) // 13 = **0** ✓
            14 (Karo Ass)
            14 // 13 = **1** ✓
            (14-1) // 13 = **1** ✓
            26 (Karo König)
            26 // 13 = **2** ❌
            (26-1) // 13 = **1** ✓'''



def straight(gezogene):
    """
    Prüft, ob die gezogenen Karten eine Straße bilden.
    Eine Straße besteht aus 5 aufeinanderfolgenden Werten.
    Beispiel: [2, 3, 4, 5, 6] oder [10, 11, 12, 13, 1] (10–Ass)
    """
    werte = kartenwerte(gezogene)
    werte.sort()

    # Normale Straße prüfen (z. B. 5–6–7–8–9)
    if all(werte[i] == werte[i - 1] + 1 for i in range(1, len(werte))):
        return True

    # Sonderfall: Ass-hoch-Straße (10–Bube–Dame–König–Ass)
    if werte == [1, 10, 11, 12, 13]:
        return True

    return False


def drilling(gezogene):
    """
    Prüft, ob ein Drilling vorhanden ist (drei gleiche Werte).
    Beispiel: [7, 7, 7, 2, 10]
    """
    werte = kartenwerte(gezogene)
    for wert in werte:
        if werte.count(wert) == 3:
            return True
    return False


def zweiPaare(gezogene):
    """
    Prüft, ob zwei verschiedene Paare vorhanden sind.
    Beispiel: [5, 5, 9, 9, 12]
    """
    werte = kartenwerte(gezogene)
    paare = 0

    # Alle Werte durchgehen
    for wert in set(werte):
        if werte.count(wert) == 2:
            paare += 1

    return paare == 2


def paar(gezogene):
    """
    Prüft, ob es mindestens ein Paar gibt (zwei gleiche Werte).
    Beispiel: [5, 5, 7, 9, 12]
    """
    werte = kartenwerte(gezogene)
    for wert in werte:
        if werte.count(wert) == 2:
            return True
    return False



if __name__ == "__main__":
    alle_Karten = karten_Zuteilen()     ### Karten einfügen
    vorkommen = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 100000):         ### 100000 mal ausführen
        gezogene = ziehung(alle_Karten)     ### die Zahlen ziehen
        gezogene = sorted(gezogene)

        if flush(gezogene):
            vorkommen[4] += 1
        elif straight(gezogene):
            vorkommen[3] += 1
        elif drilling(gezogene):
            vorkommen[2] += 1
        elif zweiPaare(gezogene):
            vorkommen[1] += 1
        elif paar(gezogene):
            vorkommen[0] += 1

    for wahrscheinlichkeit in vorkommen:
        print(wahrscheinlichkeit / 100000)      ### Wahrscheinlichkeiten ausgeben