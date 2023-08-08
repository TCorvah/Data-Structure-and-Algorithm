from collections import defaultdict
import sys
import math
import collections

#edge class for neighbor and cost
class Edge():
    def __init__(self, neighbor, cost) -> None:
        self.neighbor = neighbor
        self.cost = math.fabs(cost)

    def __str__(self) -> str:
        return "(" + str(self.neighbor)

 #a directed graph implementation using adjacency list 
class Graph:
    def __init__(self):
        self.graphMatrix = {}


    # add nodes to the graph, does not take duplicate as this is directed.
    def addNodes(self, node):
        if node in self.graphMatrix.keys():
            return False
        self.graphMatrix[node] = []
        return True
    

    #add edge to the graph, nodes must be present or else an error is thrown
    def addEdge(self, start, dest, cost):
        if start not in self.graphMatrix.keys() or dest not in self.graphMatrix.keys():
            print("error, both nodes must be present in the graph")
        #edge = Edge(dest, cost)
        #edge.neighbor = dest
        #edge.cost = cost
        self.graphMatrix[start] = [dest, math.fabs(cost)]
        return self.graphMatrix
    
    # check if two nodes have edge in common
    def hasEdge(self, start, dest):
        n1 = []
        if start in self.graphMatrix:
            n1 = self.graphMatrix[start]
            if dest in n1:
                print(start, "have a direct edge with ",dest)
                return True
            print(start, "does not have a direct edge with ",dest)
            return False
    
    #remove specific edge from the graph
    def removeEdge(self, start, dest):
        n1 = self.graphMatrix[start]
        if self.hasEdge(start, dest) == True:
            n1.remove(dest)
        else:
            print(" no direct edge from", start, "to", dest)
        return self.graphMatrix
    #provides a view of prior edges
    def edgesFrom(self, node):
        arcs =  self.graphMatrix.get(node)
        if arcs == None:
            print("source node does not exist")
        return list(arcs)
    
    # iterates throu each node in the graph
    def iterator(self):
        lst = []
        for k in self.graphMatrix.keys():
            lst.append(k)
        return lst
    

g = Graph()
print(g.addNodes(0))
print(g.addNodes(5))
print(g.addNodes(4))
print(g.addNodes(7))
print(g.addEdge(0, 5, 9))
print(g.addEdge(5, 4, 3))
print(g.hasEdge(0, 4))
print(g.removeEdge(0, 5))
print(g.edgesFrom(0))
print(g.edgesFrom(5))
print(g.iterator())






        

