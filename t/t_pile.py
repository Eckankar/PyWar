from pile import *
from deck import *
import unittest

class PileTests(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.pile = Pile()

    def testInitialSetup(self):
        self.assertEquals(self.pile.cardsLeft(), 0)

    def testAddSingle(self):
        card = self.deck.peekCard()

        self.pile.addCard(self.deck.popCard())

        self.assertEquals(self.pile.cardsLeft(), 1)
        self.assertEquals(self.pile.peekCard(), card)
        self.assertEquals(self.pile.popCard(), card)
        self.assertEquals(self.pile.cardsLeft(), 0)

    def testAddMultiple(self):
        card1 = self.deck.popCard()
        card2 = self.deck.popCard()

        self.pile.addCard(card1)
        self.pile.addCard(card2)

        self.assertEquals(self.pile.cardsLeft(), 2)
        self.assertEquals(self.pile.peekCard(), card1)
        self.assertEquals(self.pile.popCard(), card1)

        self.assertEquals(self.pile.cardsLeft(), 1)
        self.assertEquals(self.pile.peekCard(), card2)
        self.assertEquals(self.pile.popCard(), card2)

        self.assertEquals(self.pile.cardsLeft(), 0)
