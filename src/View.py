#Take gameboard and print it to the screen
from Board import Board
from Card import Card
b = Board(4)


cells = b.getFreeCells()
cells[0] = Card(0, 11)
cells[1] = Card(0, 6)
cells[2] = Card(0, 3)
cells[3] = Card(0, 4)
found = b.getFoundations()
tabs = b.getTableaus()
def updateView(board):

    print("Free Cells------------------Foundations\n")
    BoardStrs = []
    for card in cells:
        BoardStrs.append(card.toString())
    for card in found:
        BoardStrs.append(card.toString())
    fcellprint(BoardStrs)
    print("\n---------------------------------------\n")
    BoardStrs.clear()
    for i in range(7):
        tabstrs = []
        for j in range(8):
            tabstrs.append(tabs[i][j].toString())
        fcellprint(tabstrs)

    #Print the board
    #print(b.freeCells[0].toString(), b.freeCells[1].toString(), b.freeCells[2].toString(), b.freeCells[3].toString())
    
    #for i in range(len(b.freeCells)):
        #print (fcellprint(b.freeCells[i]))

#https://stackoverflow.com/questions/43372078/how-to-print-multiline-strings-on-the-same-line-in-python
def fcellprint(strings):
    strings_by_column = [s.split('\n') for s in strings]

    # Group the split strings by line
    # In this example, all strings are the same, so for each line we
    # will have three copies of the same string.
    strings_by_line = zip(*strings_by_column)

    # Work out how much space we will need for the longest line of
    # each multiline string
    max_length_by_column = [
        max([len(s) for s in col_strings])
        for col_strings in strings_by_column
    ]

    for parts in strings_by_line:
        # Pad strings in each column so they are the same length
        padded_strings = [
            parts[i].ljust(max_length_by_column[i])
            for i in range(len(parts))
        ]
        print(''.join(padded_strings))
#https://stackoverflow.com/questions/39230209/how-to-print-2-lists-vertically-next-to-each-other
updateView(b)