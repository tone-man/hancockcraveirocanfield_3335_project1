# Object that represents the deck of cards for the FreeCell game.
from Card import Card
import random

class Deck:

    def __init__(self):
        """ Initalize the deck by making an empty array and filling it with cards.
        0 = Spades
        1 = Clubs
        2 = Hearts
        3 = Diamonds

        Keyword arguments:
        i -- 4 times 
        j -- 1 - 13
        4 * 13 = 52 cards
        """
        self.fullDeck = []

        for i in range(0, 4):
            for j in range (1, 14):
                self.fullDeck.append(Card(i, j))
    
    

    def shuffle(self):
        """Shuffles the deck using the random library

        Keyword arguments:
        shuffle -- uses the Fisher-Yates shuffle
        """
        random.shuffle(self.fullDeck)


    def getTopC(self):
        """Returns or draws the last card in the deck.
        """
        return self.fullDeck.pop()    




    
