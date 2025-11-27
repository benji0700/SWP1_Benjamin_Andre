import unittest
from Poker.Pokersimulator import zweiPaare, drilling, flush

class TestPokerSimulation(unittest.TestCase):

    def test_zweiPaare(self):
        ergebnis = zweiPaare([5, 5, 7, 9, 12])
        self.assertEqual(ergebnis, False)
        print("ZweiPaare gefunden!")
        self.assertIsNot(ergebnis, True)


if __name__ == '__main__':
    unittest.main()