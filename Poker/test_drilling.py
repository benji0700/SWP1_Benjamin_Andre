import unittest
from Poker.Pokersimulator import drilling

class TestPokerSimulation(unittest.TestCase):

    def test_drilling(self):
        ergebnis = drilling([5, 5, 7, 9, 12])
        self.assertEqual(ergebnis, False)

        ergebnis2 = drilling([5, 5, 8, 5, 10])
        self.assertEqual(ergebnis2, True)
        print("Drilling gefunden!")

if __name__ == '__main__':
    unittest.main()