from getch import getch
import os

class TextUI:
    def displayWelcome(self):
        print """ :::  ===  === :::====  :::==== 
 :::  ===  === :::  === :::  ===
 ===  ===  === ======== ======= 
  ===========  ===  === === === 
   ==== ====   ===  === ===  ===
"""

    def promptForPlayers(self):
        num = 0

        while num < 2 or num > 8:
            num = int(raw_input("Please input number of players (2-8): "))

        names = []
        for i in range(num):
            name = ""
            while name == "":
                name = raw_input("Name of Player "+str(i+1)+": ")
            names.append(name)

        print ""

        return names

    def pressKeyToContinue(self):
        print "Press a key...",
        getch()
        print ""

    def preGame(self, game):
        print "Let the game begin!";
        self.pressKeyToContinue()

    def displayTurn(self, game):
        os.system('clear')
        moves = game.lastMove

        for move in moves:
            self.displayMove(move)

        print ""

        print "Card tally:"
        for player in game.players:
            left = player.pile.cardsLeft()
            plural = "s"
            if left == 1:
                plural = ""
            print player.name(), "has", left, "card"+plural, "left."

        self.pressKeyToContinue()

    def displayMove(self, move):
        if move == 'allTooFewTie':
            print "No one has enough cards to complete it!"
            print "There's a tie for the most cards, so no one wins!"
        elif move == 'warStart':
            print "We have a war!"
        elif move == 'warStartNoCards':
            print "No one has any cards to fight in it, though!"
        elif move[0] == 'full':
            for (player, card) in move[1]:
                print player.name(), "turns over the", card.name() + "."
        elif move[0] == 'win':
            print move[1].name(), "wins the round!"
        elif move[0] == 'warNoContest':
            print move[1].name(), "wins per default as they're the only one with cards left."
        elif move[0] == 'allTooFewWin':
            print "No one has enough cards to complete it!"
            print move[1].name(), "wins by having the most cards."
        elif move[0] == 'tooFew':
            for player in move[1]:
                print player.name(), "has too few cards to complete the war."
        elif move[0] == 'fullWar':
            for (player, card) in move[1]:
                print player.name(), "deals 3 cards face down."
            for (player, card) in move[1]:
                print player.name(), "turns over the", card.name() + "."
        else:
            print move[0]


    def displayGameOver(self, game):
        print ""
        winner = game.activePlayers()[0]
        print winner.name(), "has won the game!"
        print ""
        print """                     :::=====  :::====  :::=======  :::=====
                     :::       :::  === ::: === === :::     
                     === ===== ======== === === === ======  
                     ===   === ===  === ===     === ===     
                      =======  ===  === ===     === ========
                                                            
                       :::====  :::  === :::===== :::==== 
                       :::  === :::  === :::      :::  ===
                       ===  === ===  === ======   ======= 
                       ===  ===  ======  ===      === === 
                        ======     ==    ======== ===  ==="""
