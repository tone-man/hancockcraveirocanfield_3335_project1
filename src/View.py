#Take gameboard and print it to the screen
from Board import Board
from Card import Card

def updateView(board):
    cells = board.getFreeCells()
    found = board.getFoundations()
    tabs = board.getTableaus()
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
updateView(b)