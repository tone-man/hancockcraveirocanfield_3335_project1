#Object that represents the board for a FreeCell game
from Card import Card

class Board:
    def __init__(self, numFreeCells):
        """Constructs a new FreeCell Board
        
        Keyword Arguments:
        numFreeCells -- number of Free Cells available to the player
        """
        self.numFreeCells = numFreeCells
        self.freeCells = [] * numFreeCells
        self.tableaus = [[]] * 8
        self.foundations = [] * 4

        #insert Deck Here

        #Do Dealing here
        
    
    def reset(self):
        self.freeCells = [] * self.numFreeCells
        self.tableaus = []
        self.foundations = []

        #insert Deck Here

        #Do Dealing here

    def getFreeCells(self):
        return self.freeCells

    def getTableaus(self):
        return self.tableaus

    def getFoundations(self):
        return self.foundations
    
    def setCell(self, c, fcidx):
        self.freeCells[fcidx] = c
    
    def addToTableau(self, c, tidx):
        pass

    def popTableau(self,  )

    def setTableaus(self, tableaus):
        self.tableaus = tableaus

    def setFoundations(self, foundations):
        self.foundations = foundations
