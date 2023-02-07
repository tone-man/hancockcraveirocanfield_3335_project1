#Object that represents the board for a FreeCell game
class Board:
    def __init__(self, numFreeCells):
        self.freeCells = [[]] * numFreeCells
        self.tableaus = [[]] * 8
        self.foundations = [] * 4
    
    def reset(self):
        self.freeCells = []
        self.tableaus = []
        self.foundations = []