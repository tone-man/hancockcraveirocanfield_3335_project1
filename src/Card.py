#Object that represents a card for a FreeCell game
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def getNumber(self):
        return self.number

    def getSuit(self):
        return self.suit