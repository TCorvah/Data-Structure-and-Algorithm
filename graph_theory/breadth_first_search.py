from collections import defaultdict

class Node:
    def __init__(self,key):    
        self.key = key
        self.right = None
        self.dist = 0
        

# A doubly linklist queue implementation using breadth first search algorithm
# with head and tail pointer fo front and back of the queue
class Queue:
    def __init__(self):
        self.front = self.tail = None   
        self.dist = 0
    
        

    def isEmpty(self):
        """Returns true if queue is empty, otherwise returns False"""
        return self.front is None
                
    def enqueue(self, value):
        """This function adds a new element at the back of the queuue
            if the queue is empty, then the element becomes the first queue item
        """      
        node = Node(value)
        if self.isEmpty():
            self.front = self.tail = node
            self.dist = 0
        else:
            self.tail.right = node
            self.tail = node
            
    def dequeue(self):
        """ Remove the first item added in the queue and return the data of
            the remove queue element 
        """
        if self.isEmpty():
            print("queue is empty\n")
            return None
        else:
            temp = self.front.key
            self.front = self.front.right
            if not self.front:
                self.tail = None
        return temp

    def PrintQueue(self):
        """Prints the queue element and it nearest neighbor in the directed
            graphs in a First in first out manner
        """
        print("elements in queue\n")
        queue = self.front
        while queue:
            print("Queue -> {}\n".format(queue.key), end="")
            queue = queue.right
        print("None\n")
        
#A graph class using adjacency list representation. in this implementation, a directed
# graph is being used. the graph class initialize the number of vertices, visited set and the queue class
class Graph:
    def __init__(self, numVertices):
        """Initialize graph with the given number of vertices."""
        self.v = numVertices
        self.adjlist = defaultdict(list)
        self.visited = set() 
        self.queue = Queue()
        self.pred = {} 
      

        
    def addEdge(self, src, dest):
        """Add an undirected edge between src and dest."""
        temp = self.adjlist[src]
        while temp:
            if temp.key == dest:
                return  # Edge already exists
            temp = temp.right
    
        # Add edge from src to dest
        srcNode = Node(dest)
        srcNode.right = self.adjlist[src]
        self.adjlist[src] = srcNode
    
        # Add edge from dest to src
        destNode = Node(src)
        destNode.right = self.adjlist[dest]
        self.adjlist[dest] = destNode
        
        
    def printGraph(self):
        """Print the adjacency list of the graph."""
        for i in range(self.v):
            if i in self.adjlist:  # Check if the vertex has an adjacency list
                temp = self.adjlist[i]
                print("Adjacency list of vertex {}\n head ".format(i), end=" ")
                while temp:
                    print(" -> {}".format(temp.key), end="")
                    temp = temp.right
                print(" \n")
            else:
                print(f"Adjacency list of vertex {i}\n head None \n")
            
    def bfs(self,startVertex):
        """Perform BFS traversal starting from startVertex."""
        if startVertex not in self.adjlist:
            print(f"Error: Start vertex {startVertex} does not exist in the graph.")
            return
        self.visited.clear()
        self.queue.enqueue(startVertex) 
        self.visited.add(startVertex)
        print(f"Starting BFS from vertex {startVertex}...\n")
        
        while not self.queue.isEmpty(): 
            self.queue.PrintQueue() 
            currentVertex = self.queue.dequeue()
            print(f"Visited vertex: {currentVertex}") 
             
            # iterate through all adjacency vertices 
            temp = self.adjlist[currentVertex] 
            while temp:
                adjvertex = temp.key 
                if adjvertex not in self.visited:
                    self.visited.add(adjvertex)  
                    self.queue.enqueue(adjvertex) 
                temp = temp.right         
           
        print("\nBFS traversal completed.\n")
        
        
def main():   
    print("Welcome to the Graph Operations Program!")
    numVertices = int(input("Enter number of vertices: "))
    graph = Graph(numVertices)
    while True:
            print("\nChoose an operation:")
            print("1.  Add Edge\n")
            print("2.  Print Graph\n")
            print("3.  BFS\n")
            print("4.  Exit\n")
            choice = int(input("Enter your choice: ")) 
                   
            if choice == 1:
                 user_input = input("Enter source and destination:  ")
                 src, dest = tuple(int(item) for item in user_input.split())
                 print(src,dest)
                 graph.addEdge(src, dest)
                 
            elif choice == 2:
                 graph.printGraph()
                 
            elif choice == 3:    
                 startVertex = int(input("Enter starting vertex:  "))
                 print("starting vertex:",startVertex)
                 graph.bfs(startVertex)
                 
            elif choice == 4:
                 print("bye\n")
                 break
            else:
                 print("Invalid choice")
if __name__ == "__main__":
    main()