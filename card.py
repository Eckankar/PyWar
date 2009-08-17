class Card:
    """ 
        Suits: 
        1 = clubs
        2 = diamonds
        3 = hearts
        4 = spades
    """
    suit  = 0
    """
        Values:
        2 - 10 = 2 - 10
        11 = jack
        12 = queen
        13 = king
        14 = ace
    """
    value = 0

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def name(self):
        output = ""

        output += {  2: "Two",
                     3: "Three",
                     4: "Four",
                     5: "Five",
                     6: "Six",
                     7: "Seven",
                     8: "Eight",
                     9: "Nine",
                    10: "Ten",
                    11: "Jack",
                    12: "Queen",
                    13: "King",
                    14: "Ace" }[self.value]

        output += " of "
        output += { 1: "Clubs",
                    2: "Diamonds",
                    3: "Hearts",
                    4: "Spades" }[self.suit]
        return output

    def compare(self, other):
        if self.value > other.value:
            return 1
        elif self.value < other.value:
            return -1
        else:
            return 0

    def __repr__(self):
        output = ""

        output += {  2: "2",
                     3: "3",
                     4: "4",
                     5: "5",
                     6: "6",
                     7: "7",
                     8: "8",
                     9: "9",
                    10: "T",
                    11: "J",
                    12: "Q",
                    13: "K",
                    14: "A" }[self.value]

        output += { 1: "C",
                    2: "D",
                    3: "H",
                    4: "S" }[self.suit]
        return output

    def __hash__(self):
        return self.value

    def __cmp__(self, other):
        return self.compare(other)

    def __eq__(self, other):
        return self.value == other.value and self.suit  == other.suit
