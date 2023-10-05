import math

class AStarHeuristics():  

    def heuristics(self,nodeA, nodeB, heuristicFunction):
        if heuristicFunction == "euclidean":
            return math.dist(nodeA, nodeB)


    def getWeight(source, dest):
       return math.dist(source, dest)


        
