#Object that represents the board for a FreeCell game
from Card import Card

class Board:
    def __init__(self, numFreeCells):
        """Constructs a new FreeCell Board
        
        Keyword Arguments:
        numFreeCells -- number of Free Cells available to the player
        """
        self.freeCells = [Card(None,None) for x in range(numFreeCells)]
        self.tableaus = [[Card(None,None) for x in range(8)] for x in range(7)]
        self.foundations = [Card(None,None)] * 4

        #insert Deck Here

        #Do Dealing here
        
    
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

    def getTableau(idx):
        return self.tableaus[idx]

    def getFoundations(self):
        return self.foundations
    
    def setCell(self, c, fcidx):
        self.freeCells[fcidx] = c

    def setTableaus(self, tableaus):
        self.tableaus = tableaus

    def setFoundations(self, foundations):
        self.foundations = foundations
