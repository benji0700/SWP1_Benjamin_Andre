class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht

    def __str__(self):
        return f"{self.name} ({self.geschlecht})"


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht):
        super().__init__(name, geschlecht)

    def __str__(self):
        return f"{self.name} ({self.geschlecht})"


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht):
        super().__init__(name, geschlecht)

    def __str__(self):
        return f"{self.name} ({self.geschlecht}) - Abteilungsleiter*in"

class Firma:
    def __init__(self, firmaName, abteilungen):
        self.firmaName = firmaName
        self.abteilungen = abteilungen

    def info(self):
        abteilungsInfos = [abteilung.info() for abteilung in self.abteilungen]
        return f"Firma: {self.firmaName}\n" + "\n".join(abteilungsInfos)

    def count_mitarbeiter(self):
        erg = 0
        for abteilung in self.abteilungen:
            erg += len(abteilung.mitarbeiter)
        return erg

    def print_abteilungen(self):
        return ", ".join([str(a) for a in self.abteilungen])

    def geschlechter_anteil(self):
        frauen = 0
        maenner = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.geschlecht == "w":
                    frauen += 1
                else:
                    maenner += 1
        gesamt = frauen + maenner
        frauen_prozent = (frauen / gesamt * 100) if gesamt > 0 else 0
        maenner_prozent = (maenner / gesamt * 100) if gesamt > 0 else 0
        return frauen_prozent, maenner_prozent


class Abteilung:
    def __init__(self, abteilungsName, abteilungsleiter, mitarbeiter):
        self.abteilungsname = abteilungsName
        self.mitarbeiter = mitarbeiter
        self.abteilungsleiter = abteilungsleiter

    def info(self):
        mitarbeiterNamen = ", ".join([str(m) for m in self.mitarbeiter])
        return f"Abteilung: {self.abteilungsname}\nLeiter: { self.abteilungsleiter}\nMitarbeiter: {mitarbeiterNamen}\n"

    def __str__(self):
        return f"{self.abteilungsname}"

    def abteilungen(self):
        return self.abteilungen()


def most_mitarbeiter(abteilungen):
    max_abteilung = None
    max_count = 0
    for a in abteilungen:
        if len(a.mitarbeiter) > max_count:
            max_count = len(a.mitarbeiter)
            max_abteilung = a
    return max_abteilung


if __name__ == "__main__":
    ### Abteilung 1
    m1 = Mitarbeiter(name="Andi", geschlecht="m")
    m2 = Mitarbeiter(name="Chris", geschlecht="m")
    al1 = Abteilungsleiter(name="Annabell", geschlecht="w")
    a_it = Abteilung("IT", al1, [m1, m2])

    ### Abteilung 2
    m3 = Mitarbeiter(name="Iris", geschlecht="w")
    m4 = Mitarbeiter(name="Benji", geschlecht="m")
    m5 = Mitarbeiter(name="Hons", geschlecht="m")
    m6 = Mitarbeiter(name="Dori", geschlecht="w")
    al2 = Abteilungsleiter(name="Marc", geschlecht="m")
    a_production = Abteilung("Produktion", al2, [m3, m4, m5, m6])

    ### Abteilung 3
    m7 = Mitarbeiter(name="Joana", geschlecht="w")
    m8 = Mitarbeiter(name="Fitzi", geschlecht="m")
    m9 = Mitarbeiter(name="Rubner", geschlecht="m")
    al3 = Abteilungsleiter(name="Jank", geschlecht="m")
    a_sales = Abteilung("Verkauf", al3, [m7, m8, m9])

    ### Firma erstellen
    firma = Firma("Benji Pi", [a_it, a_production, a_sales])
    print(firma.info())


    ### Methoden
    print(f"Anzahl Mitarbeitern*innen: {firma.count_mitarbeiter()}")
    print(f"Abteilungen: {firma.print_abteilungen()}")

    ### Abteilung mit größter Mitarbeiterstärke
    groesste_abteilung = most_mitarbeiter(firma.abteilungen)
    print(f"Abteilung mit den meisten Mitarbeitern: {groesste_abteilung.abteilungsname} ({len(groesste_abteilung.mitarbeiter)} Mitarbeiter)")

    ### Geschlechteranteil
    frauen_prozent, maenner_prozent = firma.geschlechter_anteil()
    print(f"Geschlechteranteil - Frauen: {frauen_prozent:.2f}%, Männer: {maenner_prozent:.2f}%")
