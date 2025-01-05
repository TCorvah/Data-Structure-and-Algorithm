from breadth_first_search import Graph
from nodes import Node
from collections import deque



def BFS_ShortestPath(graph, startVertex, dest):  
        graph = Graph()     
        start = Node(startVertex)
        start.key = startVertex
        start.dist = 0
        end = Node(dest)
        end.key = dest
        start.left = None
        graph.visited.add(start.key)
        graph.queue.enqueue(start.key) 
        if start == end:
            print(start)
            return  
        while not graph.queue.isEmpty(): 
            graph.queue.PrintQueue() 
            currentVertex = graph.queue.dequeue() 
            print("visited node <- {}\n".format(currentVertex), end="")              
            temp = graph.adjlist[currentVertex]         
            while temp:
                adjvertex = temp.key  
                n = Node(adjvertex)
                n.dist = Node(currentVertex).dist + 1
                print(n.dist)    
                if adjvertex not in graph.visited:          
                    graph.visited.add(adjvertex) 
                    graph.queue.enqueue(adjvertex)   
                    graph.pred[adjvertex] = currentVertex
                if adjvertex == end.key:
                    return reconstructPath(graph.pred,start.key, end.key) 
                temp = temp.right          
        print(" \n")  
        
def reconstructPath(pred, source, dest):
    path = deque()
    current = dest
    while current != source:
        path.appendleft(current)
        current = pred.get(current)
        if current is None:
            print("no path from", source, "to",dest)
        dist = len(list(path))
        print("shortest path has distance", dist)
        path.appendleft(source)
        x = print(list(path))
        return x
    
    
