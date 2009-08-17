from player import *
import unittest

class PlayerTests(unittest.TestCase):

    def setUp(self):
        self.player = Player("Thomas")

    def testSanity(self):
        self.assertEquals(self.player.name(), "Thomas")
        self.assertEquals(self.player.pile.cardsLeft(), 0)
