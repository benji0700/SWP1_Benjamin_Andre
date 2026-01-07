class Fahrzeug:
    def __init__(self, marke, max_geschwindigkeit):
        self.marke = marke
        self.max_geschwindigkeit = max_geschwindigkeit

    def info(self):
        return f"Marke: {self.marke}, Max. Geschw.: {self.max_geschwindigkeit} km/h"


class Auto(Fahrzeug):
    def __init__(self, marke, max_geschwindigkeit, anzahl_tueren):
        super().__init__(marke, max_geschwindigkeit)
        self.anzahl_tueren = anzahl_tueren

    def info(self):
        return super().info() + ", Türen: {self.anzahl_tueren}"


class Audi(Auto):
    def __init__(self, max_geschwindigkeit, anzahl_tueren, modell):
        super().__init__("Audi", max_geschwindigkeit, anzahl_tueren)
        self.modell = modell

    def info(self):
        return super().info() + ", Modell: {self.modell}"


if __name__ == "__main__":
    mein_auto = Audi(250, 4, "A6")
    print(mein_auto.info())