import unittest
from Poker.Pokersimulator import paar, zweiPaare, drilling, flush

class TestPokerSimulation(unittest.TestCase):

    def test_flush(self):
        ergebnis = flush([2, 11, 3, 4, 6])
        self.assertEqual(ergebnis, True)
        print("Flush gefunden!")

        ergebnis2 = flush([2, 4, 6, 8, 10])
        self.assertEqual(ergebnis2, True)
        print("Flush gefunden!")

if __name__ == '__main__':
    unittest.main()