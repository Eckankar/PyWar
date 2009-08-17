
class Pile:
    def __init__(self):
        self.cards = []

    def cardsLeft(self):
        return len(self.cards)

    def addCard(self, card):
        self.cards.append(card)

    def peekCard(self):
        return self.cards[0]

    def popCard(self):
        return self.cards.pop(0)
