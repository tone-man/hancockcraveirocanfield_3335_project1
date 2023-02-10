#Object that represents a card for a FreeCell game
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def getNumber(self):
        return self.number

    def getSuit(self):
        return self.suit
    
    def toString(self):
        num = self.getNumber()
        suit = self.getSuit()
        if num == None and suit == None:
            return "---- \n" + "|   | \n" + "---- "
        if num == '10':
            return self.number + "-- \n" + self.suit + "  | \n" + "---- "
        return self.number + "--- \n" + self.suit + "  | \n" + "---- "