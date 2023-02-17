from Board import Board
from Queue import PriorityQueue
from GameController import GameController
from Card import Card
from copy import deepcopy
from View import View
from Node import Node

class gameAgent:
    def __init__(self, b: Board, c: GameController):
        '''
        Creates a gameAgent to solve FreeCell.

        Keyword arguments:
        b -- the board itself, in its initial state
        c -- controller for agent to interact with board
        '''
        self.b = b
        self.controller = c
        self.maxNodes = 100

    def solve(self):
        '''
        Solves the freeCell game, given the board it was given.
        '''

        self.search(self.b)
        #self.execute()

    
    def search(self, b : Board) -> list:
        '''
        Searches state space using MBA* (Memory Bounded A*) to find
        goal state. If goal state is not found before reaching memory
        cap, it will return path to best possible state.
        '''
        node = Node(b, 1) #root Tuple
        path = [node]

        if self.isGoal(self.b):
            return path
        
        frontier = PriorityQueue()
        frontier.pqPush(node, 1)

        reached = [b] #if we have reached a state, we should not check it again

        while not (frontier.isEmpty() and len(reached) < self.maxNodes):
            node = frontier.pqPop()
            print(node)
            self.expand(node) #Find node's children

            for child in node.next:
                c = child.data

                if self.isGoal(c):
                    path.append(child)
                    return path

                elif (reached.count(c) == 0):
                    reached.insert(0, c)
                    #insert h calc here
                    newNode = Node(c, 1)
                    frontier.pqPush(newNode, 1)

        return path

    def expand(self, node: Node) -> None:
        '''
        Expands node n to find children in state space

        Keyword arguments:
        node -- node in question
        '''
        board = node.data #get the boards state

        #simulate moving top tab card to another tab

        curTab = 0 #counter to reduce repeat checking

        tabs = board.getTableaus()
        freeCells = board.getFreeCells()
        foundations = board.getFoundations()

        for t in range(len(tabs)):
            card = tabs[t][0]

            for i in range(len(tabs)):

                if t == i:
                    pass
                
                if self.controller.isValidMoveForTab(card, tabs[i]):
                    copyB = deepcopy(board) # making a deep copy of board to make a new state
                    copyTabs = copyB.getTableaus()

                    copyC = copyTabs[t].pop(0)
                    copyTabs[i].insert(0, copyC)

                    node.addNext(Node(copyB, 1))
    
            curTab += 1
        
        #simulate to freeCell and foundation movements
        for t in range(len(tabs)):
            card = tabs[t][0]

            for i in range(len(freeCells)):
                
                #tab to freeCell
                if self.controller.isValidMoveForFreeCell(card, i):
                    copyB = deepcopy(board)
                    copyTab = copyB.getTableau(t)
                    copyFC = copyB.getFreeCells()

                    copyC = copyTab.pop(0)
                    copyFC[i] = copyC

                    node.addNext(Node(copyB, 1))
                    break
            
                #tab to foundation
            if self.controller.isValidMoveForFoundation(card):
                copyB = deepcopy(board)
                copyTab = copyB.getTableau(t)
                copyF = copyB.getFoundations()

                copyC = copyTab.pop(0)
                copyF[copyC.getSuit()] = copyC

                node.addNext(Node(copyB, 1))

        #simulate from freeCell movements to tabs and foundations
        for i in range(len(freeCells)):
            card = freeCells[i]

            if (card != None): #Only do this if cell is NOT empty
                #Card to tab
                for t in range(len(tabs)):
                    if(self.controller.isValidMoveForTab(card, tabs[t])):
                        copyB = deepcopy(board)
                        copyTab = copyB.getTableau(t)
                        copyFC = copyB.getFreeCells()

                        copyC = copyFC[i]
                        copyTab.insert(0, copyC)
                        copyFC = None

                        node.addNext(Node(copyB, 1))
                #Card to foundation
                
                if(self.controller.isValidMoveForFoundation(card)):
                    copyB = deepcopy(board)
                    copyF = copyB.getFoundations()
                    copyFC = copyB.getFreeCells()

                    copyC = copyFC[i]
                    copyF[copyC.getSuit()] = copyC
                    copyC = None

                    node.addNext(Node(copyB, 1))
    

    def execute(self) -> None:
        '''
        Executes moves given a path.
        '''
        pass

    def isGoal(self, s :Board) -> None:
        '''
        Checks if the board is in a goal state.

        Keyword arguments:
        s -- board to check
        '''
        
        numgoals = 0
        for f in s.getFoundations():
            if isinstance(f, Card):
                if f.getNumber() == 13:
                    numgoals += 1
        if numgoals == 4:
            return True
        else:
            return False

    def freeCellHeuristicWilliam(self, node):
        print("FreeCell Heuristic")
        
    def freeCellHeuristicRyan(self, node):
        print("FreeCell Heuristic")

    def freeCellHeuristicAntonio(self, node):
        print("FreeCell Heuristic")