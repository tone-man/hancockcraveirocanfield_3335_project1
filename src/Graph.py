from Queue import Node 

class Graph:
    """Constructs the Graph for a* search.

    ## Note: this is an undirected graph meaning that all nodes are connected together and edges are bidirectional

        Keyword arguments:
        data -- data or cards that go into the node
        p -- priority/heuristic for the nodes
        Nodes -- are the Nodes/Vertices
    """

    # A graph is a list of list
    # Initializing the graph with size as # of nodes

    hn = Node(1, 1)
    def __init__(self, nodes):
        self.N = nodes
        self.graph = [None] * self.N
 
    # adds edge to and from nodes
    def add_edge(self, start, end):
        """adds edge 

        Keyword arguments:
        start -- source node
        end -- destination node
    """
        # Adds a node to the start node
        node = Node(end)
        node.next = self.graph[start]
        self.graph[start] = node
 
       # A adds a node to the end node
        node = Node(start)
        node.next = self.graph[end]
        self.graph[end] = node
 
    # Print the graph
    def print_graph(self):
        for i in range(self.N):
            print("Adjacency list of vertex {}\n head".format(i), end = "")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
 
 
# Test Code 
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
 
    graph.print_graph()
 
# Source: Geeks for Geeks by Kanav Malhotra