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
        self.nodeMap = NodeData().NodeDict
        self.graph = Graph()
        self.entries = {}
        self.closelist = NodeData().visited
        self.neighbor = self
       

    def getShortestPath(self,source, dest, heuristics):
        heuristics = AStarHeuristic.AStarHeuristics
        sourcedata = NodeData(source)
        sourcedata.setGcost(0)
        fScore =  sourcedata.calcFCost(heuristics.getWeight(source,dest))
        self.nodeMap[source] = sourcedata
        self.entries[sourcedata] = self.queue.insert(sourcedata,fScore)
        path = {} 
        closeList = self.closelist
        while not self.queue.isEmpty:
            nodedata  = self.queue.extractMin()
            extract_node = NodeData(nodedata)
            if extract_node.getNode() == dest:
                return(list(tuple(self.reconstructPath(path, dest), extract_node.getGcost)))
            closeList.add(extract_node)
            for neighborEntry in self.graph.edgesFrom(extract_node.getNode()):
            #for neighbor in graph.edgesFrom(nodedata.getNode()):         
                entrynode = neighborEntry        
                if entrynode in self.nodeMap.keys():
                    self.neighbor = self.nodeMap.get(entrynode)
                else:
                    self.neighbor = NodeData(entrynode)
                    self.nodeMap[entrynode].append(self.neighbor)
                if self.neighbor in closeList:
                    continue
                distanceBtwnNodes = neighborEntry
                tentativeGscore = distanceBtwnNodes + extract_node.getGcost()
                if tentativeGscore < self.neighbor.getGcost():
                    self.neighbor.setGcost(tentativeGscore)
                    fScore = self.neighbor.calcFCost(heuristics.getWeight(self.neighbor.getNode(), dest))
                    path.append((self.neighbor.getNode(), extract_node.getNode()))
                    if self.neighbor not in self.entries:
                        self.entries[self.neighbor] =  self.queue.insert(self.neighbor, fScore)
                    else:
                       self.queue.fib_decrease(self.entries.get(self.neighbor.getNode()), fScore)

        return None
    
    def reconstructPath(self,path, dest):
        assert len(path) != 0
        assert dest != None
        pathList = []
        pathList.append(dest)
        while dest in path.keys():
            dest = path.get(dest)
            pathList.append(dest)
        pathList.reverse()
        return pathList





   





             

         

           




     
        
        
        
        



        
 



    

    