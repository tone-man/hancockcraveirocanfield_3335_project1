#Object that represents the board for a FreeCell game
class Board:
    def __init__(self, numFreeCells):
        self.freeCells = [0 for x in range(numFreeCells)]
        self.tableaus = [[]] * 8
        self.foundations = [] * 4
    
    def reset(self):
        self.freeCells = []
        self.tableaus = []
        self.foundations = []

    def getFreeCells(self):
        return self.freeCells

    def getTableaus(self):
        return self.tableaus

    def getFoundations(self):
        return self.foundations
    
    def setFreeCells(self, freeCells):
        self.freeCells = freeCells

    def setTableaus(self, tableaus):
        self.tableaus = tableaus

    def setFoundations(self, foundations):
        self.foundations = foundations