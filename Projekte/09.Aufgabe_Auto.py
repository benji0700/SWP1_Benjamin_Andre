class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __len__(self):
        return self.ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        return "Addition nur mit Auto-Objekten möglich!"

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        return "Subtraktion nur mit Auto-Objekten möglich!"

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        return "Multiplikation nur mit Auto-Objekten möglich!"

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return False

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return False

if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)
    a3 = Auto(50)

    print(len(a1))

    print(a1 + a2)

    print(a2 - a1)

    print(a1 * a2)

    print(a1 == a3)
    print(a1 == a2)

    print(a1 < a2)

    print(a2 > a1)

    print(a1 + 5)
