from Board import Board
from Queue import PriorityQueue
from GameController import GameController
from Card import Card
from copy import deepcopy
from View import View
from Node import Node
import time

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
        self.failureFlag = False
        self.maxNodes = 1500 

    def solve(self):
        '''
        Solves the freeCell game, given the board it was given.
        '''
        print("Agent Initiated!")
        i = 0
        while (not self.failureFlag) and (not self.isGoal(self.b)):

            print("Round :", i)
            print("-------------------------")
            print("Searching State Space...")

            path = self.search(self.b) #returns solution path to input in controller

            if self.failureFlag:
                print("Search ran out of states")

            print("Search Complete")
            print("Beginning Execution")
            print("-------------------------")
            self.execute(path)

            i += 1

        if self.failureFlag:
            print("Goal State Unreachable, Agent Shutting Down")
        else:
            print("Goal State has been reached, Agent Shutting Down")

    def search(self, b : Board) -> list:
        '''
        Searches state space using MBA* (Memory Bounded A*) to find
        goal state. If goal state is not found before reaching memory
        cap, it will return path to best possible state.
        '''
        node = Node(b, 1, None, 0, 0, 0) #root Tuple
        path = []
        if self.isGoal(self.b):
            return path
        
        frontier = PriorityQueue()
        frontier.pqPush(node, 1)

        reached = [b] #if we have reached a state, we should not check it again
        reachedCount = 0 #this limits the len of reached to keep the code efficient

        while not (frontier.isEmpty() or len(reached) > self.maxNodes):
            node = frontier.pqPop()
            self.expand(node) #Find node's children

            for child in node.next:
                c = child.data

                if self.isGoal(c):
                    while child.parent != None:
                        path.append(child)
                        child = child.parent
                    v = View()
                    v.updateView(c)
                    return path

                elif (reached.count(c) == 0):
                    reached.append(c)

                    #insert h calc here
                    newNode = Node(c, node.hval + self.basicHueristic(c), node, child.movetype, child.src, child.dest)
                    frontier.pqPush(newNode, newNode.hval)

        if frontier.isEmpty():
            self.failureFlag = True

        while node.parent != None:
            path.append(node)
            node = node.parent
        return path

    def expand(self, node: Node) -> None:
        '''
        Expands node n to find children in state space

        Keyword arguments:
        node -- node in question
        '''
        board = node.data #get the boards state

        #simulate moving top tab card to another tab

        tabs = board.getTableaus()

        freeCells = board.getFreeCells()
        foundations = board.getFoundations()

        for t in range(len(tabs)):

            if(len(tabs[t]) > 0):

                card = tabs[t][0]
                src = t
                emptyTabCount = 0 #Count of empty tabs, we ignore placements of cards past the first one
                                  #This reduces state spaces so we do not cycle when cards get low

                for i in range(len(tabs)):

                    if t == i:
                        pass

                    if(len(tabs[i]) == 0):
                        emptyTabCount += 1

                    #moveCardBetweenTabs
                    if emptyTabCount == 0 and self.isValidMoveForTab(card, tabs[i]) :
                        copyB = deepcopy(board) # making a deep copy of board to make a new state
                        copyTabs = copyB.getTableaus()

                        copyC = copyTabs[t].pop(0)
                        copyTabs[i].insert(0, copyC)
                        node.addNext(Node(copyB, 1, node, 1, src, i))
        
        #simulate to freeCell and foundation movements
        for t in range(len(tabs)):

            if(len(tabs[t]) > 0):
                card = tabs[t][0]
                src = t
                for i in range(len(freeCells)):
                    
                    #tab to freeCell
                    #moveCardToFreeCell
                    if freeCells[i] == None:
                        copyB = deepcopy(board)
                        copyTab = copyB.getTableau(t)
                        copyFC = copyB.getFreeCells()

                        copyC = copyTab.pop(0)
                        copyFC[i] = copyC

                        node.addNext(Node(copyB, 1, node, 2, src, i))
                        break
            
                #tab to foundation
                #moveTabtoFoundation
                if self.isValidMoveForFoundation(board, card):
                    copyB = deepcopy(board)
                    copyTab = copyB.getTableau(t)
                    copyF = copyB.getFoundations()

                    copyC = copyTab.pop(0)
                    copyF[copyC.getSuit()] = copyC
                    
                    node.addNext(Node(copyB, 1, node, 4, src, copyC.getSuit()))

        #simulate from freeCell movements to tabs and foundations
        for i in range(len(freeCells)):
            card = freeCells[i]
            emptyTabCount = 0 #Same counter from before when simulating tabtotab

            if (card != None): #Only do this if cell is NOT empty
                #Card to tab
                #moveCardFromFreeCell
                for t in range(len(tabs)):
                    
                    if(len(tabs) == 0):
                        emptyTabCount += 1

                    if emptyTabCount == 0 and self.isValidMoveForTab(card, tabs[t]):
                        copyB = deepcopy(board)
                        copyTab = copyB.getTableau(t)
                        copyFC = copyB.getFreeCells()

                        copyC = copyFC[i]
                        copyTab.insert(0, copyC)
                        copyFC[i] = None

                        node.addNext(Node(copyB, 1, node, 3, i, t))

                #Card to foundation
                #moveFreeCelltoFoundation
                if(self.isValidMoveForFoundation(board, card)):
                    copyB = deepcopy(board)
                    copyF = copyB.getFoundations()
                    copyFC = copyB.getFreeCells()

                    copyC = copyFC[i]
                    copyF[copyC.getSuit()] = copyC
                    copyFC[i] = None
                    
                    node.addNext(Node(copyB, 1, node, 5, i, copyC.getSuit()))
    
    def execute(self, path) -> None:
        '''
        Executes moves given a path.

        Keyword arguments:
        path -- path to execute
        '''
        path.reverse()
        if path == None:
            exit()
        for node in path:
            if node.movetype == 1:
                print("Move card from tab", node.src + 1, "to tab", node.dest + 1)
                self.controller.moveCardBetweenTabs(node.src, node.dest)
            elif node.movetype == 2:
                print("Move card from tab", node.src + 1, "to free cell", node.dest + 1)
                self.controller.moveCardToFreeCell(node.src, node.dest)
            elif node.movetype == 3:
                print("Move card from free cell", node.src + 1, "to tab", node.dest + 1)
                self.controller.moveCardFromFreeCell(node.src, node.dest)
            elif node.movetype == 4:
                print("Move card from tab", node.src + 1, "to foundation", node.dest + 1)
                self.controller.moveTabtoFoundation(node.src)
            elif node.movetype == 5:
                print("Move card from free cell", node.src + 1, "to foundation", node.dest + 1)
                self.controller.moveFreeCelltoFoundation(node.src)
            time.sleep(.25)
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

    def freeCellHeuristicWilliam(self, b: Board):
        h = 0

        idx = 0
        foundations = b.getFoundations()
        for foundation in foundations:
            if foundation == None:
                cardval = 0
            else:
                cardval = foundation.getNumber()
            suit = idx
            for tableau in b.getTableaus():
                for card in tableau:
                    if card.getNumber() == cardval + 1 and card.getSuit() == suit:
                        #get the number of cards below it
                        if tableau.index(card) == 0:
                            numcards = 0
                        else:
                            numcards = tableau.index(card) - 1
                        h += numcards
            idx += 1
        for f in foundations:
            cardsOfSuitLeft = 0

            if f:
                cardsOfSuitLeft = f.getNumber()

            h += (13 - cardsOfSuitLeft)
        return h
        
    def basicHueristic(self, b: Board):
        h = 0
        foundations = b.getFoundations()
        for f in foundations:
            cardsOfSuitLeft = 0
            if f:
                cardsOfSuitLeft = f.getNumber()
            h += (13 - cardsOfSuitLeft)
        return h

    def freeCellHeuristicAntonio(self, b: Board):
        '''
        An attempt to improve the basic hueristic by
        setting h to the how many moves it would take to sort the board,
        plus the cards left on the board. This h is not admissable unfortunately, as it
        double counts each movement. :(
        '''
        tabs = b.getTableaus()
        foundations = b.getFoundations()
        h = 0

        for tab in tabs:
            copytab = deepcopy(tab)
            copytab.sort()
            
            for i in range(len(tab)):
            #find distance of card from sorted card
            #each cell offset is worth 1 point
                diff = abs(i - tab.index(copytab[i]))
                h += diff

        #Added weight so foundations are prioritized
        for f in foundations:
            cardsOfSuitLeft = 0

            if f:
                cardsOfSuitLeft = f.getNumber()

            h += (13 - cardsOfSuitLeft)

        #print(h)
        return h

    def isValidMoveForTab(self, c, dt) -> bool:
        """Checks that card placement is valid.

        Keyword arguments:
        c -- card in question
        dt -- destination tableau
        """
        if c == None:
            return False

        if len(dt) == 0:
            return True

        topC = dt[0]  #Top Card of Destination Tableau

        s = c.getSuit()

        if((s == 0 or s == 1) and (topC.getSuit() == 2 or topC.getSuit() == 3)):
            if(topC.getNumber() - c.getNumber() == 1):
                return True

        elif((s == 2 or s == 3) and (topC.getSuit() == 0 or topC.getSuit() == 1)):
            if(topC.getNumber() - c.getNumber() == 1):
                return True


        return False
    
    def isValidMoveForFreeCell(self, b, c, fcIdx) -> bool:
        """Checks that card placement is valid into freecell.

        Keyword arguments:
        b -- board state
        c -- card in question
        fc -- destination freecell index
        """

        if c == None:
            return False
        f = b.getFreeCells()

        if(f[fcIdx] == None):
            return True

        return False

    
    def isValidMoveForFoundation(self, b, c) -> bool:
        """Checks that card placement is valid into foundation pile.

        Keyword arguments:
        b -- board state
        c -- card in question
        
        """
        if c == None:
            return False

        f = b.getFoundations()
        s = c.getSuit()
        v = c.getNumber()

        if(f[s] == None and v == 1):
            return True
        elif(f[s] != None):
            if(v - f[s].getNumber() == 1):
                return True
            
        return False


        