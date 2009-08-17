from pile import *

class Player:

    def __init__(self):
        self.__init__("Kerjigger")

    def __init__(self, name):
        self.myName = name
        self.pile = Pile()

    def name(self):
        return self.myName

    def __repr__(self):
        return self.name()
