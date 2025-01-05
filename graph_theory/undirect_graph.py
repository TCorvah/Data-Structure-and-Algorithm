from collections import defaultdict
from nodes import Node
#A graph class using adjacency list representation. in this implementation, an undirected
# graph is being used. the graph class initialize the number of vertices, visited set and the queue class
class Graph:
    def __init__(self, numVertices):
        self.v = numVertices
        self.adjlist = defaultdict(list)
        
    def addEdge(self, src, dest):
        #add edge from src to dest:
        newNode = Node(dest).createNode(dest)
        newNode.right = self.adjlist[src]
        self.adjlist[src] = newNode
      
        
        #add edge from dest to src:
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
