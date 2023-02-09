#Take gameboard and print it to the screen
from Board import Board
from Card import Card
b = Board(4)
cells = b.getFreeCells()
cells[0] = Card("♥", 1)
cells[1] = Card("♥", 2)
cells[2] = Card("♥", 3)
cells[3] = Card("♥", 4)
def updateView(board):
    #Print the board
    print("Free Cells:")
    for i in range(len(b.freeCells)):
        print (fcellprint(b.freeCells[i]))

def fcellprint(card):
    print( card.getNumber(), card.getSuit())
#https://stackoverflow.com/questions/39230209/how-to-print-2-lists-vertically-next-to-each-other
updateView(b)