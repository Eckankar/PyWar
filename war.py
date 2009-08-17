from game import Game
from textui import TextUI

ui = TextUI()

players = ui.displayWelcome()

players = ui.promptForPlayers()

warGame = Game(players)

ui.preGame(warGame)

while not warGame.gameOver():
    warGame.run()
    ui.displayTurn(warGame)

ui.displayGameOver(warGame)
