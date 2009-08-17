from game import *
from player import *
from card import *
import unittest

class GameTests(unittest.TestCase):

    def setUp(self):
        self.game = Game(["Logan", "Billy"])
        self.game2 = Game(["Shauna", "Leon", "Stuart"])

    def testNames(self):
        self.assertEquals(self.game.names(), ["Logan", "Billy"])
        self.assertEquals(self.game2.names(), \
            ["Shauna", "Leon", "Stuart"])

    def testEvenDistribution(self):
        sizes = self.game.pileSizes()

        self.assert_(max(sizes) <= min(sizes) + 1)

    def testSanity(self):
        self.assert_(not self.game.gameOver())
        self.assert_(not self.game2.gameOver())

    """
    def testGameOver(self):
        while not self.game2.gameOver():
            self.game2.run()
        self.assertEquals(\
            len(\
                filter(\
                    lambda n: n > 0,\
                    self.game2.pileSizes()\
                )\
            ),\
        1)
    """

    def testCardsStayInPlay(self):
        i = 0
        while (not self.game2.gameOver()) and i < 200:
            self.game2.run()
            self.assertEquals(\
                sum(self.game2.pileSizes()) + self.game2.removed,\
                52\
            )
            i += 1
        self.assertEquals(\
            sum(self.game2.pileSizes()) + self.game2.removed,\
            52\
        )

    def testWar(self):
        player1 = Player("Tom")

        player1.pile.addCard(Card(3,1))
        player1.pile.addCard(Card(3,2)) # Unimportant cards
        player1.pile.addCard(Card(3,3))

        player1.pile.addCard(Card(4,14)) # Ace of Spades

        player2 = Player("Bob")

        player2.pile.addCard(Card(3,4))
        player2.pile.addCard(Card(3,5)) # Unimportant cards
        player2.pile.addCard(Card(3,6))

        player2.pile.addCard(Card(4,2)) # Two of Spades

        (winner, wonCards) = self.game.war([player1, player2])

        self.assertEquals(winner, player1)

        allCards = [Card(3,1), Card(3,2), Card(3,3),\
                    Card(3,4), Card(3,5), Card(3,6),\
                    Card(4,14), Card(4,2)]

        self.assertEquals(len(set(allCards) - set(wonCards)), 0)
        self.assertEquals(len(set(allCards) & set(wonCards)), 8)
