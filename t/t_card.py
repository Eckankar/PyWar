from card import *
import unittest

class CardTests(unittest.TestCase):

    def setUp(self):
        self.aceOfSpades = Card(4, 14)
        self.aceOfDiamonds = Card(2, 14)
        self.kingOfClubs = Card(1, 13)
        self.fiveOfHearts = Card(3, 5)

    def testNames(self):
        self.assertEqual(self.aceOfSpades.name(), "Ace of Spades")
        self.assertEqual(self.aceOfDiamonds.name(), "Ace of Diamonds")
        self.assertEqual(self.kingOfClubs.name(), "King of Clubs")
        self.assertEqual(self.fiveOfHearts.name(), "Five of Hearts")

    def testCompareSelf(self):
        self.assertEqual(self.aceOfSpades.compare(self.aceOfSpades), 0)
        self.assertEqual(self.aceOfDiamonds.compare(self.aceOfDiamonds), 0)
        self.assertEqual(self.kingOfClubs.compare(self.kingOfClubs), 0)
        self.assertEqual(self.fiveOfHearts.compare(self.fiveOfHearts), 0)

    def testCompare(self):
        self.assertEqual(self.aceOfSpades.compare(self.aceOfDiamonds), 0)
        self.assertEqual(self.aceOfDiamonds.compare(self.aceOfSpades), 0)
        self.assertEqual(self.fiveOfHearts.compare(self.kingOfClubs), -1)
        self.assertEqual(self.aceOfSpades.compare(self.kingOfClubs), 1)
