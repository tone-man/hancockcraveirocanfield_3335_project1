class pqNode:
    def __init__(self, d, p):
        self.data = d
        self.priority = p
        self.next = None


class PriorityQueue:
    """"Constructs the priority queue using linked lists

            Keyword Methods:
            isEmpty -- Checks the queue to see if it's empty
            pqPush -- Adds node based on priority
            pqPop -- Removes highest priority node and updates queue
            pqPeek -- Looks at highest priority node and prints it
            pqTraverse -- Prints out the queue
    """

    def __init__(self):

        self.front = None

    # Checks to see if the queue is empty
    def isEmpty(self):

        return True if self.front == None else False

    # Adds node to the queue based on priority
    def pqPush(self, value, priority):

        if self.isEmpty() == True:

            # Adds node if queue is empty
            self.front = pqNode(value, priority)

        else:

            # Checks first node's priority
            if self.front.priority > priority:

                newNode = pqNode(value, priority)
                newNode.next = self.front
                self.front = newNode

            else:

                # Traverses queue until node gets added
                temp = self.front

                while temp.next:

                    if priority <= temp.next.priority:
                        break
                    temp = temp.next

                newNode = pqNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode

    # Removes highest priority node and updates queue
    def pqPop(self):

        # Checks Queue
        if self.isEmpty() == True:
            return None

        else:

            # Removes pqNode with highest priority and updates the queue
            data = self.front.data
            self.front = self.front.next
            return data

    # Returns node with highest priority
    def pqPeek(self):

        # Checks queue and prints node
        if self.isEmpty() == True:
            return None
        else:
            return self.front.data

    # Prints the queue
    def pqtraverse(self):

        # Checks for priority
        if self.isEmpty() == True:
            return "The queue is empty"
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

from Node import Node
if __name__ == "__main__":

    # Test Code
    pq = PriorityQueue()
    pq.pqPush(Node(1, 1), 1)
    pq.pqPush(Node(3, 3), 3)
    pq.pqPush(Node(2, 2), 2)
    pq.pqPush(Node(0, 0), 0)
    print(pq.pqPeek())
    n = pq.pqPop()
    print(n.data)
    pq.pqtraverse()


# Data Structure found on Geeks for Geeks website and contributed by himanshu kanojiya
