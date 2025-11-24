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


def ziehung():
    karten = list(range(1, 53))
    gezogene = random.sample(karten, 5)
    return gezogene

def kartenwerte(gezogene):
    """
    Rechnet die gezogenen Karten (1–52) in Werte von 1–13 um.
    Dabei ist:
    1 = Ass, 11 = Bube, 12 = Dame, 13 = König
    """
    werte = [(karte - 1) % 13 + 1 for karte in gezogene]
    return werte

def royalFlush(gezogenen):
    werte = kartenwerte(gezogenen)
    werte.sort()    ### damit es 1, 10, 11, 12, 13 ist
    return True if (werte == [1, 10, 11, 12, 13] and flush(gezogenen)) else False

def straightFlush(gezogene):
    return True if (straight(gezogene) and flush(gezogene)) else False

def vierling(gezogene):
    werte = kartenwerte(gezogene)
    return True if any(werte.count(wert) == 4 for wert in werte) else False

def fullHouse(gezogene):
    """
    Prüft, ob die 5 gezogenen Karten ein Full House bilden.
    Ein Full House = genau 3 Karten mit dem gleichen Wert (Drilling)
                 + genau 2 Karten mit einem anderen gleichen Wert (Paar).
    Erwartet: 'gezogene' ist eine Liste von Kartennummern 1–52.
    Liefert: True wenn Full House, sonst False.
    """

    # 1) Werte (1–13) aus den Kartennummern berechnen
    #    (z. B. 1=Ass, 11=Bube, 12=Dame, 13=König)
    werte = kartenwerte(gezogene)

    # 2) Ein Full House hat genau 2 verschiedene Werte.
    #    Wenn es nicht genau 2 sind, kann es kein Full House sein.
    einzigartige = set(werte)
    if len(einzigartige) != 2:
        return False

    # 3) Für die beiden vorhandenen Werte zählen, wie oft sie vorkommen.
    #    Beispiel: counts könnte [3,2] oder [2,3] sein.
    counts = [werte.count(w) for w in einzigartige]

    # 4) Sortieren erleichtert den Vergleich: [2,3] ist das Kennzeichen für Full House.
    counts.sort()

    # 5) Wenn die Häufigkeiten genau [2,3] sind, ist es ein Full House.
    return counts == [2, 3]


def flush(gezogene):
    gedreht = gezogene[:]   ### erstellt eine Kopie, damit nicht so viel Speicher verwendet wird! Noch googlen!
    gedreht.reverse()
    return all((gedreht[i] - 1) // 13 == (gedreht[i - 1] - 1) // 13 for i in range(1, len(gedreht)))


def straight(gezogene):
    """
    Prüft, ob die gezogenen Karten eine Straße bilden.
    Eine Straße besteht aus 5 aufeinanderfolgenden Werten.
    Beispiel: [2, 3, 4, 5, 6] oder [10, 11, 12, 13, 1] (10–Ass)
    """
    werte = kartenwerte(gezogene)
    werte.sort()

    # Normale Straße prüfen (z. B. 5–6–7–8–9)
    normale_strasse = all(werte[i] == werte[i - 1] + 1 for i in range(1, len(werte)))
    # Sonderfall: Ass-hoch-Straße (10–Bube–Dame–König–Ass)
    ass_hoch = werte == [1, 10, 11, 12, 13]

    return True if (normale_strasse or ass_hoch) else False


def drilling(gezogene):
    """
    Prüft, ob ein Drilling vorhanden ist (drei gleiche Werte).
    Beispiel: [7, 7, 7, 2, 10]
    """
    werte = kartenwerte(gezogene)
    return True if any(werte.count(wert) == 3 for wert in werte) else False


def zweiPaare(gezogene):
    """
    Prüft, ob zwei verschiedene Paare vorhanden sind.
    Beispiel: [5, 5, 9, 9, 12]
    """
    werte = kartenwerte(gezogene)
    paare = sum(1 for wert in set(werte) if werte.count(wert) == 2)
    return True if paare == 2 else False


def paar(gezogene):
    """
    Prüft, ob es mindestens ein Paar gibt (zwei gleiche Werte).
    Beispiel: [5, 5, 7, 9, 12]
    """
    werte = kartenwerte(gezogene)
    return True if any(werte.count(wert) == 2 for wert in werte) else False



if __name__ == "__main__":
    vorkommen = {
        "Paar": 0,
        "Zwei Paare": 0,
        "Drilling": 0,
        "Straight": 0,
        "Flush": 0,
        "Full House": 0,
        "Vierling": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }
    for _ in range(100000):
        gezogene = ziehung()
        gezogene = sorted(gezogene)

        vorkommen.values()
        if royalFlush(gezogene):
            vorkommen["Royal Flush"] += 1
        elif straightFlush(gezogene):
            vorkommen["Straight Flush"] += 1
        elif vierling(gezogene):
            vorkommen["Vierling"] += 1
        elif fullHouse(gezogene):
            vorkommen["Full House"] += 1
        elif flush(gezogene):
            vorkommen["Flush"] += 1
        elif straight(gezogene):
            vorkommen["Straight"] += 1
        elif drilling(gezogene):
            vorkommen["Drilling"] += 1
        elif zweiPaare(gezogene):
            vorkommen["Zwei Paare"] += 1
        elif paar(gezogene):
            vorkommen["Paar"] += 1

    for hand, count in vorkommen.items():
        wahrscheinlichkeit = count / 100000  # 100000 = Gesamtzahl der Ziehungen
        print(f"{hand}: {wahrscheinlichkeit:.6f}")