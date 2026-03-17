import random

class zahlen():
    def __init__(self, zahl):
        self.zahl = zahl
        self.naechstes = None

    def setNextElement(self, zahl):
        self.naechstes = zahl

    def getNextElement(self):
        return self.naechstes

    def returnElement(self):
        return self.zahl


class Liste():
    def __init__(self):
        self.start = None

    def addObject(self, objekt):

        if self.start is None:
            self.start = objekt
            return

        vorheriges = self.start

        while vorheriges.getNextElement() is not None:
            vorheriges = vorheriges.getNextElement()

        vorheriges.setNextElement(objekt)

    def length(self):
        count = 0
        aktuelles = self.start

        while aktuelles is not None:
            count += 1
            aktuelles = aktuelles.getNextElement()

        return count

    def printAll(self):
        aktuelles = self.start

        while aktuelles is not None:
            print(aktuelles.returnElement())
            aktuelles = aktuelles.getNextElement()

    def __iter__(self):
        aktuelles = self.start

        while aktuelles is not None:
            yield aktuelles.returnElement()
            aktuelles = aktuelles.getNextElement()


if __name__ == "__main__":

    liste = Liste()

    for i in range(5):
        zahl = random.randint(1, 100)
        objekt = zahlen(zahl)
        liste.addObject(objekt)

    print("Alle Elemente:")
    liste.printAll()

    print("Länge der Liste:", liste.length())

    print("Iterator Ausgabe:")
    for x in liste:
        print(x)