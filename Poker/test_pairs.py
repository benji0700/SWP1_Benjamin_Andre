import unittest
from Poker.Pokersimulator import paar, zweiPaare, drilling, flush

class TestPokerSimulation(unittest.TestCase):
    def test_paar(self):
        ergebnis = paar([5, 5, 7, 9, 12])
        self.assertEqual(ergebnis, True)
        print("Paar gefunden!")

if __name__ == '__main__':
    unittest.main()