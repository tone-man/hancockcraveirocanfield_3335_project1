
class pqNode:
    """Constructs the node for the priority queue used in the a* search.

        Keyword arguments:
        data -- data or cards that go into the node
        p -- priority orders the nodes
        next -- gets the next node
    """

	
    def __init__(self, value, p):
        self.data = value
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
			return
		
		else:
			
			# Removes Node with highest priority and updates the queue
			self.front = self.front.next
			return  
			
	# Returns node with highest priority
	def pqPeek(self):
		
		# Checks queue and prints node
		if self.isEmpty() == True:
			return
		else:
			print(self.front.data) 
			
	# Prints the queue
	def pqtraverse(self):

		# Checks for priority
		if self.isEmpty() == True:
			return "The queue is empty"
		else:
			temp = self.front
			while temp:
				print(temp.data, end = " ")
				temp = temp.next


if __name__ == "__main__":
	
# Test Code 
	pq = PriorityQueue()
	pq.pqPush(8, 1)
	pq.pqPush(6, 3)
	pq.pqPush(5, 2)
	pq.pqPush(7, 0)
	pq.pqPeek()
	pq.pqPop()
	pq.pqtraverse()
	

	
	
# Data Structure found on Geeks for Geeks website and contributed by himanshu kanojiya