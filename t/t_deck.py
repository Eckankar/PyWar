from deck import *
import unittest

class DeckTests(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck2 = Deck()

    def test52DifferentCards(self):
        self.assertEquals(self.deck.cardsLeft(), 52)

        removed = []
        i = 0
        while self.deck.cardsLeft() > 0 and i < 52:
            i+=1
            removed.append(self.deck.popCard().name())

        self.assertEquals(self.deck.cardsLeft(), 0)
        self.assertEquals(i, 52)

        self.assertEquals(len(set(removed)), 52)

    def testPopPeek(self):
        top = self.deck.peekCard()
        self.assertEquals(self.deck.cardsLeft(), 52)
        self.assertEquals(self.deck.popCard(), top)
        self.assertEquals(self.deck.cardsLeft(), 51)

    def testShuffle(self):
        self.deck.shuffle()

        deckOne = []
        deckTwo = []
        while self.deck.cardsLeft() > 0 and self.deck2.cardsLeft() > 0:
            deckOne.append(self.deck.popCard().name())
            deckTwo.append(self.deck2.popCard().name())

        self.assertEquals(self.deck.cardsLeft(), 0)
        self.assertEquals(self.deck2.cardsLeft(), 0)
        self.assertEquals(set(deckOne), set(deckTwo))
