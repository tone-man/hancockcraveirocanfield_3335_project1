class Node:
    """Constructs the node for the A* Search.

    Keyword arguments:
    data -- data or cards that go into the node
    p -- priority/heuristic for the nodes
    next -- list of nodes children
    transition -- tuple defining state trasnisiton function
    """
    def __init__(self, value, h, p, m, s, d):
        self.data = value
        self.hval = h
        self.next = []  # All edges of this node
        self.parent = p
        self.movetype = m
        self.src = s
        self.dest = d

    def addNext(self, n):
        self.next.append(n)


