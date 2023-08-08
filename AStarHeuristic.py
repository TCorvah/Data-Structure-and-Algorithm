from Graph import Edge
import math
class AStarHeuristics(Edge):

    def getWeight(self,source, dest):
        first = Edge(source, self.cost)
        dest = Edge(dest, self.cost)
        return first.cost, dest.cost




v = AStarHeuristics.getWeight(5, dest=5)
print(v)