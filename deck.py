from card import Card
import random

class Deck:
    deck = []
    s = 0

    def __init__(self):
        self.deck = []
        for i in range (1, 5):
            for j in range (2, 15):
                self.deck.append(Card(i, j))
                self.s += 1

    def cardsLeft(self):
        return len(self.deck)

    def popCard(self):
        return self.deck.pop()

    def peekCard(self):
        return self.deck[-1]

    def shuffle(self):
        random.shuffle(self.deck)
