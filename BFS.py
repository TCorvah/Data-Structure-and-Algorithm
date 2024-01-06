from collections import defaultdict
class Node:
    def __init__(self,key):    
        self.key = key
        self.left = None
        self.right = None
    
    def createNode(self,data):
        node = Node(data) 
        node.key = data 
        node.right = None
        self.prev = node.left
        return node

# A singly linklist queue implementation using breadth first search algorithm
# in my implementation, there is no extra pointer for rear as the next element will be
#the rear of the front of the linklist. A single pointer is initialize for the queue class
class Queue:
    def __init__(self):
        self.front = None 
        self.tail = None 
        self.size = 0 
        

    def isEmpty(self):
        """Returns true if queue is empty, otherwise returns False"""
        if self.size == 0:
            print("queue is empty\n")
            return True
        else:
            return False
                

     
    def enqueue(self, value):
        """This function adds a new element at the back of the queuue
            if the queue is empty, then the element becomes the first queue item
        """      
        node = Node(value).createNode(value)
        if self.front == None:
            self.front = node
            self.size += 1
        else:
            temp = self.front
            while temp.right:
                temp = temp.right
            temp.right = node
            self.size += 1
            
            
 

    def dequeue(self):
        """ Remove the first item added in the queue and return the data of
            the remove queue element 
        """
        if self.isEmpty():
            print("queue is empty\n")
            return None
        else:
            temp = self.front
            self.front = self.front.right
            data = temp.key    
            temp1 = None
            temp = temp1
            self.size -= 1
            return data

    def PrintQueue(self):
        """Prints the queue element and it nearest neighbor in the directed
            graphs
        """
        print("elements in queue\n")
        queue = self.front
        while queue:
            print("Queue -> {}\n".format(queue.key), end="")
            queue = queue.right
        print("\n")


#A graph class using adjacency list representation. in this implementation, a directed
# graph is being used. the graph class initialize the number of vertices, visited set and the queue class
class Graph:
    def __init__(self, numVertices):
        self.v = numVertices
        self.adjlist = defaultdict(list)
        self.visited = set() 
        self.queue = Queue()
      

        
    def addEdge(self, src, dest):
        #add edge from src to dest:
        newNode = Node(dest).createNode(dest)
        newNode.right = self.adjlist[src]
        self.adjlist[src] = newNode
       
        newNode = Node(src).createNode(src)
        newNode.right = self.adjlist[dest]
        self.adjlist[dest] = newNode

    def  printGraph(self):
        for i in range((self.v)):
            temp = self.adjlist[i]
            print("Adjacency list of vertex {}\n head ".format(i), end=" ")   
            while temp:
                print(" -> {}".format(temp.key), end="")
                temp = temp.right
            print(" \n")

    def bfs(self,startVertex):
        start = Node(startVertex).createNode(startVertex)
        start.key = startVertex
        self.visited.add(start.key)
        self.queue.enqueue(start.key)   
        while not self.queue.isEmpty():
            self.queue.PrintQueue()  
            currentVertex = self.queue.dequeue()
            print("visited node <- {}\n".format(currentVertex), end="")     
            temp = self.adjlist[currentVertex] 
            while temp:
                adjvertex = temp.key 
                if adjvertex not in self.visited:
                    self.visited.add(adjvertex)  
                    self.queue.enqueue(adjvertex)   
                temp = temp.right         
           
        print(" \n")
           
          
              
def main():   
    print("\ninitial graph operation")
    val = int(input("Enter number of vertices: "))
    print(val)
    graph = Graph(val)
    while True:
            print("\nWhat do you want to do?\n")
            print("1. Add edge\n")
            print("2. Print graph\n")
            print("3. BFS\n")
            print("4. Exit\n")
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
