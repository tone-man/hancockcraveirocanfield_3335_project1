#Object that represents a card for a FreeCell game
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def getNumber(self):
        return self.number

    def getSuit(self):
        return self.suit
    
    def suitToChar(self):
        if self.suit == 0:
            return "♠"
        if self.suit == 1:
            return "♣"
        if self.suit == 2:
            return "♥"
        if self.suit == 3:
            return "♦"

    def toString(self):
        num = self.getNumber()
        suit = self.getSuit()
        if num == None and suit == None:
            return "---- \n" + "   | \n" + "---- "
        if num >= 10:
            if num == 10:
                numstr = "10"
            if num == 11:
                numstr = "J"
            if num == 12:
                numstr = "Q"
            if num == 13:
                numstr = "K"
            return numstr + "-- \n" + self.suitToChar() + "  | \n" + "---- "

        return str(self.number) + "--- \n" + self.suitToChar() + "  | \n" + "---- "

  