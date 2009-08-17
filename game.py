from deck import *
from player import *

class Game:
    """
        lastMove tells what happened in the last move.
        It is a list of tuples.
        The first element of the tuple is an identifier.

        Possible identifiers, formats and meanings:
        
        Identifier: full
        Tuple size: 2
        Meaning: A normal deal of one card per player.
                 #1 contains a list of tuples, (player, card dealt)

        Identifier: win
        Tuple size: 2
        Meaning: The deal was won.
                 #1 is the winner

        Identifier: warStart
        Tuple size: 1
        Meaning: A war has started.

        Identifier: warStartNoCards
        Tuple size: 1
        Meaning: No one had any cards to use for the war, so it ended
                 in a loss for all.

        Identifier: warNoContest
        Tuple size: 2
        Meaning: One player was the only one left with cards for the war,
                 and thusly won.
                 #1 is the winner
        
        Identifier: allTooFewWin
        Tuple size: 2
        Meaning: Everyone had too few cards for a complete war.
                 #1 had more cards than everyone else and thus won the war.
        
        Identifier: allTooFewTie
        Tuple size: 1
        Meaning: Everyone had too few cards, and there was a tie for most cards.
                 Everyone lost.

        
        Identifier: tooFew
        Tuple size: 2
        Meaning: Some players had too few cards to complete a war and were
                 automatically eliminated.
                 #1 is a list of those players.

        Identifier: fullWar
        Tuple size: 2
        Meaning: Full war dealt.
                 #1 is list of tuples, (player, open card dealt)
        
    """
    lastMove = []

    def __init__(self, players):
        self.players = map(lambda name: Player(name), players)

        self.removed = 0
        self.lastMove = []

        deck = Deck()
        deck.shuffle()

        num = len(players)
        (div, mod) = divmod(52, num)
        i = 0

        for player in self.players:
            pile = player.pile
            if i < mod:
                pile.addCard(deck.popCard())
            for j in range(div):
                pile.addCard(deck.popCard())
            i += 1

    def names(self):
        return map(lambda p: p.name(), self.players)

    def pileSizes(self):
        return map(lambda p: p.pile.cardsLeft(), self.players)

    def activePlayers(self):
        return filter(lambda p: p.pile.cardsLeft() > 0, self.players)

    def gameOver(self):
        return len(self.activePlayers()) <= 1

    def run(self):
        self.lastMove = []

        players = self.activePlayers()
        cards = map(lambda p: p.pile.peekCard(), players)
        self.lastMove.append(('full',\
            map(\
                lambda p: (p, p.pile.popCard()),\
                players\
            )\
        ))

        high = max(cards)
        topCards = filter(lambda c: c.value == high.value, cards)

        if len(topCards) == 1:
            winner = players[cards.index(high)]
            self.lastMove.append(('win', winner))
            for card in cards:
                winner.pile.addCard(card)
        else:
            warriors = map(lambda c: players[cards.index(c)], topCards)
            (winner, cardsWon) = self.war(warriors)

            self.lastMove.append(('win', winner))

            cardsWon.extend(cards)

            random.shuffle(cardsWon)

            if winner == None:
                removed += len(cardsWon)
            else:
                for card in cardsWon:
                    winner.pile.addCard(card)

    def war(self, warriors):
        # If you don't have enough cards for a war, you lose.
        # If multiple players don't have enough, the one with the least loses.
        # If there's a tie, both players lose
        self.lastMove.append('warStart')

        warriors = filter(lambda p: p.pile.cardsLeft() > 0, warriors)
        if len(warriors) == 0:
            self.lastMove.append('warStartNoCards')
            return (None, [])
        elif len(warriors) == 1: # Won without contest!
            self.lastMove.append(('warNoContest', warriors[0]))
            return (warriors[0], [])

        highestAmount = max(map(lambda p: p.pile.cardsLeft(), warriors))
        if 4 > highestAmount:
            highest = filter(\
                    lambda p: p.pile.cardsLeft() == highestAmount,\
                    warriors\
                )

            if len(highest) == 1:
                self.lastMove.append(('allTooFewWin', highest[0]))
                others = list(set(warriors) - set(highest))
                wonCards = []
                for player in others:
                    while player.pile.cardsLeft() > 0:
                        wonCards.append(player.pile.popCard())
                return (highest[0], wonCards)
            else:
                self.lastMove.append(('allTooFewTie'))
                return (None, [])
        else:
            discarded = []
            cards = []

            tooFew = filter(lambda p: p.pile.cardsLeft() < 4, warriors)
            if len(tooFew) > 0:
                self.lastMove.append(('tooFew', tooFew))
                for p in tooFew:
                    while p.pile.cardsLeft() > 0:
                        discarded.append(p.pile.popCard())
                    warriors.remove(p)

            for player in warriors:
                for i in range(3):
                    discarded.append(player.pile.popCard())
                cards.append(player.pile.peekCard())

            self.lastMove.append(('fullWar',\
                map(\
                    lambda p: (p, p.pile.popCard()),\
                    warriors\
                )\
            ))

            high = max(cards)
            topCards = filter(lambda c: c.value == high.value, cards)

            if len(topCards) == 1:
                winner = warriors[cards.index(high)]
                cards.extend(discarded)
                return (winner, cards)
            else:
                nextWarriors = map(lambda c: warriors[cards.index(c)], topCards)
                (winner, cardsWon) = self.war(nextWarriors)
                cardsWon.extend(cards)
                cardsWon.extend(discarded)
                return (winner, cardsWon)

