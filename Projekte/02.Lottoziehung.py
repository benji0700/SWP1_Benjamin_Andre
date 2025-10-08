import random

def initialisiere_vorkommen():
    vorkommen = {}
    for i in range(1, 46):
        vorkommen[i] = 0
    return vorkommen

def ziehung(vorkommen):
    zahl = list(range(1, 46))
    for j in range(6):
        gezogen = random.randint(0, len(zahl) - j - 1)
        gezogene_zahl = zahl[gezogen]
        vorkommen[gezogene_zahl] += 1
        letzte_position = len(zahl) - j - 1
        letzte_zahl = zahl[letzte_position]
        zahl[gezogen] = letzte_zahl
        zahl[letzte_position] = gezogene_zahl

def main():
    vorkommen = initialisiere_vorkommen()
    for i in range(100000):
        ziehung(vorkommen)
    print("Ergebnis:\n" + str(vorkommen))

if __name__ == "__main__":
    main()
