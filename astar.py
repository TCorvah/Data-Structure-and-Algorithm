from collections import defaultdict
import sys
import math
from graph import Graph
from  fibonacciHeap import FibTree
import AStarHeuristic
    
class  NodeData(object):
    def __init__(self, node):
       self.node = node
       self.gCost = float("inf")
       self.fCost = math.fabs(0.0)
       self.NodeDict = {}
       self.visited = set()

    def getNode(self):
        return self.node    
    
    def getGcost(self):
        return float(self.gCost)
    
    def setGcost(self, gCost):
        self.gCost = gCost

    def calcFCost(self, heuristic):
        self.fCost = heuristic + self.gCost
        return self.fCost
    
    def getFCost(self):
        return self.fCost
           

class NodeComparator(NodeData):
    def __init__(self):
        self.first = NodeData.getFCost
        self.second = NodeData.getFCost

    def compare(self, first, second):
        first = self.first
        second = self.second
        if first > second:
            return 1
        if second > first:
            return -1
        return 0
        
    
class AStar():
    def __init__(self):
        self.queue = FibTree()
        self.nodeMap = NodeData()
    def getShortestPath(self,graph, source, dest, heuristics):
        NodeMap = NodeData().NodeDict
        heapEntries = NodeData().NodeDict,
        heuristics = AStarHeuristic.AStarHeuristics
        graph = Graph()
        sourcedata = NodeData(source)
        sourcedata.setGcost(0)
        fScore =  sourcedata.calcFCost(heuristics.getWeight(source,dest))
        NodeMap.append((source, sourcedata))
        heapEntries.append(sourcedata,self.queue.insert(sourcedata,fScore))
        path = {} 
        closeList = NodeData().visited
        while not self.queue.isEmpty:
            nodedata  = NodeData(self.queue.extractMin()) 
            if nodedata.getNode() == dest:
                return(list(tuple(self.reconstructPath(path, dest), nodedata.getGcost())))
            closeList.add(nodedata)
            neighborEntry = graph.edgesFrom(nodedata.getNode())
            for key in neighborEntry:
            #for neighbor in graph.edgesFrom(nodedata.getNode()):
                entrynode = neighborEntry[key]
              
                if entrynode in NodeMap.keys():
                    ne = NodeMap.get(entrynode)
                else:
                    ne = NodeData(entrynode)
                    NodeMap.apend((entrynode, ne))
                if ne in closeList:
                    continue
                distanceBtwnNodes = neighborEntry
                tentativeGscore = distanceBtwnNodes + nodedata.getGcost()
                if tentativeGscore < ne.getGcost():
                    ne.setGcost(tentativeGscore)
                    fScore = ne.calcFCost(heuristics.getWeight(ne.getNode(), dest))
                    path.append((ne.getNode(), nodedata.getNode()))
                    if ne not in heapEntries:
                        heapEntries.append(ne, self.queue.insert(ne, fScore))
                    else:
                       self.queue.fib_decrease(heapEntries.get(ne), fScore)

        return None
    
    def reconstructPath(self,path, dest):
        assert len(path) != 0
        assert dest != None
        pathList = []
        pathList.append(dest)
        while dest in path.keys():
            dest = path[dest]
            pathList.append(dest)
        pathList.reverse()
        return pathList





   





             

         

           




     
        
        
        
        



        
 



    

    