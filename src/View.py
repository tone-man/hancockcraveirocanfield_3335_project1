# Take gameboard and print it to the screen
from Board import Board
from Card import Card


class View:
    def updateView(self, board):
        cells = board.getFreeCells()
        found = board.getFoundations()
        tabs = board.getTableaus()
        nullcard = Card(None, None)

        print("Free Cells------------------Foundations\n")
        BoardStrs = []
        for card in cells:
            if(card):
                BoardStrs.append(card.toString())
            else:
                BoardStrs.append(nullcard.toString())
        for card in found:
            if(card):
                BoardStrs.append(card.toString())
            else:
                BoardStrs.append(nullcard.toString())

        self.fcellprint(BoardStrs)
        print("\n---------------------------------------\n")
        BoardStrs.clear()
        maxArrayLen = self.find_max_list(tabs)

        count = 1
        for j in range(maxArrayLen - 1, -1, -1):
            tabstrs = []
            for i in range(len(tabs)):
                
                idx = len(tabs[i]) - count
                if (idx >= 0):
                    if tabs[i][idx] != None:
                        tabstrs.append(tabs[i][idx].toString())
                else:
                    tabstrs.append(nullcard.toString())

            self.fcellprint(tabstrs)
            count += 1

    # https://stackoverflow.com/questions/43372078/how-to-print-multiline-strings-on-the-same-line-in-python
    def fcellprint(self, strings):
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

    def find_max_list(self, list):
        list_len = []
        for i in list:
            list_len.append(len(i))
        return(max(list_len))
