class Node:
    """Constructs the node for the A* Search.

    Keyword arguments:
    data -- data or cards that go into the node
    p -- priority/heuristic for the nodes
    next -- list of nodes children
    transition -- tuple defining state trasnisiton function
    """

    def __init__(self, value, h):
        self.data = value
        self.hval = h
        self.next = []  # All edges of this node
        self.parent = None

    def __init__(self, value, h, p, m):
        self.data = value
        self.hval = h
        self.next = []  # All edges of this node
        self.parent = p
        self.movetype = m

    def addNext(self, n):
        self.next.append(n)


