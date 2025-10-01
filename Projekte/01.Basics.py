# if-Anweisung: Entscheidung treffen
x = 10
if x > 5:
    print("x ist größer als 5")

# for-Schleife: Über eine Sequenz iterieren
for i in range(3):
    print("Durchlauf:", i)

# while-Schleife: Solange eine Bedingung wahr ist, wiederholen
count = 0
while count < 3:
    print("Zähler:", count)
    count += 1

# break: Schleife vorzeitig beenden
for i in range(10):
    if i == 5:
        break  # Schleife wird abgebrochen, wenn i == 5
    print(i)

# continue: Nächster Schleifendurchlauf, wenn Bedingung erfüllt
for i in range(5):
    if i % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print("Ungerade Zahl:", i)

# pass: Platzhalter, tut nichts
for i in range(3):
    if i == 1:
        pass  # Hier könnte später Code stehen
    print("Index:", i)

# try-except-else-finally: Fehlerbehandlung mit allen Blöcken
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division durch Null ist nicht erlaubt")
else:
    print("Ergebnis:", result)  # Wird nur ausgeführt, wenn kein Fehler auftritt
finally:
    print("Berechnung abgeschlossen")  # Wird immer ausgeführt