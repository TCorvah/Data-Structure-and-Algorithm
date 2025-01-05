from breadth_first_search import Graph, Node, Queue
from collections import deque


def BFS_ShortestPath(graph, startVertex, dest):  
    """
    Find the shortest path from start to dest using BFS.
    Args:
        graph: Graph object containing adjacency list.
        start: Starting vertex.
        dest: Destination vertex.
    Returns:
        List representing the shortest path from start to dest.
    """ 
    # If the start and destination are the same, return immediately
    if startVertex == dest:
        print(f"Start and destination are the same: {startVertex}")
        return [startVertex]  
    
    graph.visited.clear()  # Clear the visited set
    graph.queue.enqueue(startVertex)  # Add the starting vertex to the queue
    graph.visited.add(startVertex)  # Mark the starting vertex as visited
    graph.pred[startVertex] = None  # Starting point has no predecessor
    
    # Initialize distances dictionary to track distances from the start vertex
    distances = {startVertex: 0}
    
    while not graph.queue.isEmpty(): 
        graph.queue.PrintQueue()  # Print the queue (for debugging)
        currentVertex = graph.queue.dequeue()  # Get the current vertex from the queue
        print("Visited node <- {}\n".format(currentVertex), end="")              
        
        # Traverse all adjacent vertices of the current vertex
        temp = graph.adjlist[currentVertex]         
        while temp:
            adjvertex = temp.key  # Get the adjacent vertex
            
            # If the adjacent vertex has not been visited, mark it as visited
            if adjvertex not in graph.visited:          
                graph.visited.add(adjvertex) 
                graph.queue.enqueue(adjvertex)  # Add the adjacent vertex to the queue   
                graph.pred[adjvertex] = currentVertex  # Record the predecessor
                
                # Update the distance for the adjacent vertex
                distances[adjvertex] = distances[currentVertex] + 1
                
                # If the destination is found, reconstruct the path
                if adjvertex == dest:
                    print(f"Found destination {dest}")
                    return reconstructPath(graph.pred, startVertex, dest)
            
            temp = temp.right  # Move to the next adjacent vertex
    
    print(f"No path found from {startVertex} to {dest}")
    return []  # Return an empty list if no path is found
        
    
def reconstructPath(pred, source, dest):
    """
    Reconstructs the path from source to destination using the predecessors.
    Args:
        pred: A dictionary of predecessors.
        source: The starting vertex.
        dest: The destination vertex.
    Returns:
        A list representing the path from source to dest.
    """
    path = deque()
    current = dest
    
    # Build the path by following predecessors
    while current != source:
        path.appendleft(current)
        current = pred.get(current)
        if current is None:
            print("No path from", source, "to", dest)
            return []  # Return an empty list if no path exists
    
    path.appendleft(source)  # Add the source to the beginning of the path
    print(f"Shortest path (distance {len(path) - 1}): {list(path)}")
    return list(path)


# Example usage (Graph initialization and calling BFS_ShortestPath)
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(3, 4)

    start_vertex = 0
    end_vertex = 4
    shortest_path = BFS_ShortestPath(g, start_vertex, end_vertex)
    print("Result:", shortest_path)