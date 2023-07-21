from collections import defaultdict

class Node:
    def __init__(self,vertex):
        self.vertex = vertex
        self.next = None

class Queue:
  def __init__(self):
     self.front = None
       

  def isEmpty(self):
      if self.front ==  None:
         print("queue is empty\n")
         return True
      else:
          return False
      
         
  def enqueue(self, value):
      node = Node(value)
      if self.isEmpty():
          self.front = node
      else:
          temp = self.front
          while temp.next:
                temp= temp.next
          temp.next = node
               

  def dequeue(self):
      data = Node(self.front.vertex)
      temp = self.front
      self.front = (self.front).next
      del temp
      return data.vertex
     
            
  def PrintQueue(self):
      print("elements in queue\n")
      queue = self.front
      while queue:
            print("Queue -> {}\n".format(queue.vertex), end="")
            queue = queue.next
      print("\n")

class Graph:
    def __init__(self, numVertices):
        self.v = numVertices
        self.adjlist = defaultdict(list)
        self.visited = set() 
        self.front = None
               
            
    def addEdge(self, src, dest):
        #add edge from src to dest:
        newNode = Node(dest)
        newNode.next = self.adjlist[src]
        self.adjlist[src] = newNode
        #add edge from dest to src:  
        newNode = Node(src)       
        newNode.next = self.adjlist[dest]
        self.adjlist[dest] = newNode


    def  printGraph(self):
        for i in range(self.v):
            temp = self.adjlist[i]
            print("Adjacency list of vertex {}\n head ".format(i), end=" ")   
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    def bfs(self,startVertex): 
        queue = Queue()
        queue.enqueue(startVertex)  
        self.visited.add(startVertex)  
        for i in range( self.v):
            temp = self.adjlist[i]
            while temp:
                queue.PrintQueue() 
                queue.enqueue(temp.vertex) 
                self.visited.add(temp.vertex)                
                currentVertex = queue.dequeue()
                print("deque item -> {}\n".format(currentVertex), end="")    
                temp  = temp.next
          
              
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

