from collections import defaultdict
import time
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def createNode(self,data):
        node = Node(data) 
        node.data = data 
        node.next = None
        return node
        

class Stack:
    def __init__(self):
        self.front = None 
        
    
    def isEmpty(self):
        
        """Returns true if queue is empty, otherwise returns False"""
        if self.front == None:
            print("stack is empty\n")
            return True
        else:
            return False

   
    def push(self, value):
        """This function adds a new element at the back of the queuue
            if the queue is empty, then the element becomes the first queue item
        """      
        node = Node(value)
        node.data = value
        if self.front == None:
            node.next = None
        node.next = self.front 
        self.front = node 
              
    def pop(self):
        """ Remove the first item added in the queue and return the data of
            the remove queue element 
        """
        if self.isEmpty():
            print("queue is empty\n")
            return None
        else:
            temp = self.front
            self.front = self.front.next
            data = temp.data   
            temp1 = None
            temp = temp1
            return data
    
    def PrintStack(self):
        """Prints the queue element and it nearest neighbor in the directed
            graphs
        """
        queue = self.front
        print("stack elements\n head", end = "")  
        while queue is not None:
            print("stack -> {}\n".format(queue.data), end="")
            queue = queue.next
        print("\n")
  


#A graph class using adjacency list representation. in this implementation, a directed
# graph is being used. the graph class initialize the number of vertices, visited set and the queue class
class Graph:
    def __init__(self, numVertices):
        self.v = numVertices
        self.adjlist = defaultdict(list)
        self.visited = set() 
        self.stack = Stack()
        self.time = time
        
        
    def addEdge(self, src, dest):
        #add edge from src to dest:
        newNode = Node(dest).createNode(dest)
        newNode.next = self.adjlist[src]
        self.adjlist[src] = newNode
       
        newNode = Node(src).createNode(src)
        newNode.next = self.adjlist[dest]
        self.adjlist[dest] = newNode

    def  printGraph(self):
        for i in range((self.v)):
            temp = self.adjlist[i]
            print("Adjacency list of vertex {}\n head ".format(i), end=" ")   
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")
            
    def DFS(self, startVertex):
        start = Node(startVertex).createNode(startVertex)
        start.data = startVertex
        self.stack.push(start.data)
        while not self.stack.isEmpty():
            self.stack.PrintStack() 
            currentVertex = self.stack.pop() 
            if currentVertex not in self.visited:
                self.visited.add(currentVertex)
            print("visited node <- {}\n".format(currentVertex), end="")  
            curr = self.adjlist[currentVertex]    
            while curr:
                adjvertex = curr.data 
                if adjvertex not in self.visited:
                    self.visited.add(adjvertex)            
                    self.stack.push(adjvertex)  
                curr = curr.next       
        return self.visited    
           
                 
        
        
def main():   
    print("\ninitial graph operation")
    val = int(input("Enter number of vertices: "))
    print(val)
    graph = Graph(val)
    while True:
            print("\nWhat do you want to do?\n")
            print("1. Add edge\n")
            print("2. Print graph\n")
            print("3. DFS\n")
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
                 graph.DFS(startVertex)
            elif choice == 4:
                 print("bye\n")
                 break
            else:
                 print("Invalid choice")
if __name__ == "__main__":
    main()
