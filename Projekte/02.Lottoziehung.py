import random

vorkommen = {}

for i in range(1, 46):
    vorkommen[i] = 0

for i in range(1000):
    zahl = list(range(1, 46))
    for j in range(6):
        gezogen = random.randint(0, len(zahl) - j - 1)
        gezogene_zahl = zahl[gezogen]

        vorkommen[gezogene_zahl] += 1
        letzte_position = len(zahl) - j - 1
        letzte_zahl = zahl[letzte_position]

        zahl[gezogen] = letzte_zahl
        zahl[letzte_position] = gezogene_zahl

print("Ergebnis:\n" + str(vorkommen))