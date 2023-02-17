from Board import Board
from Queue import pqNode, PriorityQueue
from Card import Card

class gameAgent:
    def __init__(self, b, c):
        '''
        Creates a gameAgent to solve FreeCell.

        Keyword arguments:
        b -- the board itself, in its initial state
        c -- controller for agent to interact with board
        '''
        self.b = b
        self.c = c
        self.maxNodes = 100

    def solve(self):
        '''
        Solves the freeCell game, given the board it was given.
        '''

        self.search(self.b)
        self.execute()


        pass
    
    def search(self, b):
        '''
        Searches state space using MBA* (Memory Bounded A*) to find
        goal state. If goal state is not found before reaching memory
        cap, it will return best possible state.
        '''

        node = pqNode(b, 1, None)
        if self.isGoal(self.b):
            return node
        
        frontier = PriorityQueue()
        reached = [node]

        while not (frontier.isEmpty() and len(reached) < self.maxNodes):
            node = frontier.pqPop()
            self.expand(node) #Find node's children

            for child in node.next:
                b = child.data

                if self.isGoal(b):
                    return child
                if reached.index(b) == -1:
                    reached.push(b)
                    frontier.pqPush(child, child.priority)

        #Need to return failure somehow

    def expand(self, n) -> None:
        '''
        Expands node n to find children in state space

        Keyword arguments:
        n -- node in question
        '''

        pass

    def execute(self) -> None:
        '''
        Executes moves given a path.
        '''
        pass

    def isGoal(s :Board) -> None:
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