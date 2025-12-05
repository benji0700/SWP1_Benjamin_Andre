'''
Aufgabe:
names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

Erzeuge aus diesen Listen eine gefilterte Liste von Personen, die folgende Bedingungen erfüllt:

Alter ≥ 18 und Score ≥ 80

müssen verwendet werden:

zip – kombiniere die drei Listen so, dass jeder Eintrag ein Tupel (name, age, score) ist.

filter + lambda – filtere alle Personen heraus, die beide Bedingungen erfüllen.

map + lambda – forme jedes Tupel in ein Dictionary der Form
{"name": ..., "age": ..., "score": ...} um.

{"name": "Anna", "age": 23, "score": 88}
'''

def ersteFilterung(names, ages, scores):
    zusammen = zip(names, ages, scores)
    erg = list(filter(lambda zs: zs[1] >= 18 and zs[2] >= 80, zusammen))
    return erg

def dicFormen(erg):
    dicErg = list(map(lambda e: {"name": e[0], "age": e[1], "score": e[2]}, erg))
    return dicErg

if __name__ == "__main__":
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]

    erg = ersteFilterung(names, ages, scores)
    dictionaryErg = dicFormen(erg)
    print(dictionaryErg)