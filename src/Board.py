#Object that represents the board for a FreeCell game
from Card import Card
from Deck import Deck 

class Board:
    def __init__(self, numFreeCells):
        """Constructs a new FreeCell Board
        
        Keyword Arguments:
        numFreeCells -- number of Free Cells available to the player
        """
        self.freeCells = [None for x in range(numFreeCells)]
        self.tableaus = [[] for x in range(8)]
        self.foundations = [None] * 4

        # Creating a new deck
        newDeck = Deck()
        # Shuffling the deck
        newDeck.shuffle()

        # Do Dealing here
        for i in range(0, 6):
            for j in range(0, 8):
                    self.tableaus[j].insert(0, newDeck.getTopC())  

        for i in range(0,4):
            c = newDeck.getTopC()
            self.tableaus[i].insert(0, c)
        
        
        
    
    def reset(self, numFreeCells):
        self.freeCells = [0 for x in range(numFreeCells)]
        self.tableaus = [[0]] * 8
        self.foundations = [0] * 4

        #insert Deck Here

        #Do Dealing here

    def getFreeCells(self):
        return self.freeCells

    def getTableaus(self):
        return self.tableaus

    def getTableau(self, idx):
        return self.tableaus[idx]

    def getFoundations(self):
        return self.foundations
    
    def setCell(self, c, fcidx):
        self.freeCells[fcidx] = c

    def setTableaus(self, tableaus):
        self.tableaus = tableaus

    def setFoundations(self, foundations):
        self.foundations = foundations

    def __eq__(self, o):
        
        if not isinstance(o, Board):
            return False

        for i in range(len(self.tableaus)):

            # Equality of Tabs
            oTab = o.getTableau(i)
            if(len(self.tableaus[i]) != len(oTab)):
                return False

            for j in range(len(self.tableaus[i])):
                if self.tableaus[i][j] != oTab[j]:
                    return False
            
        # Equality of Freecells
        oFreeCell = o.getFreeCells

        for i in len(self.freeCells):
            if self.freeCells[i] != oFreeCell[i]:
                return False

        #Knowing the tabs and freecells are equal allows us to conclude the foundations are also equal
        return True
