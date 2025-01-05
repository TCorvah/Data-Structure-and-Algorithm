
from collections import defaultdict

from dfs_path import DFSNodes, DFStack, NodeState

class DFSGraph:
    def __init__(self, numVertices):
        self.v = numVertices
        self.adjlist = defaultdict(list)
        self.visited = set()
        self.stack = DFStack()
        self.map = {}
        self.time = 0
        self.head = None

    def createNode(self,data):
        """Creates a new new node 

        Args:
            data (node): creates a new node pointer
            for each vertex in the graph

        Returns:
            data (node): A pointer to the node
        """
        node = DFSNodes(data)
        node.data = data
        node.color = NodeState.WHITE
        node.parent = None
        node.startTime = node.finishingTime = 0
        node.next = None
        return node

    def Edge(self, src, dest):
        """Turns all forward edges to backedge 
        Args: 
            src (node): creates an start node for an edge

            dest (node): creates an end node for an edge


        Returns: A reverse arc of each node
        """
        newNode = self.createNode(dest)
        newNode.data = dest
        newNode.next = self.adjlist[src]
        self.adjlist[src] = newNode

    def  printGraph(self):
        for i in range((self.v)):
            temp = self.adjlist[i]
            print("Adjacency list of vertex {}\n head ".format(i), end=" ")
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")

    def  transpose(self):
        for i in range((self.v)):
            temp = self.adjlist[i]
            print("Adjacency list of vertex {}\n head ".format(i), end=" ")
            while temp:
                print(" -> {}".format(temp.data), end="")
                self.Edge(temp.data, i)
                temp = temp.next
            print(" \n")

    def dfs(self):
        for i in range(self.v):
            self.head = self.createNode(i)
            self.head.data = i
            self.head.color = NodeState.WHITE
            self.head.parent = None
        self.time = 0
        for i in range(self.v):
            self.head = self.createNode(i)
            self.head.data = i
            if self.head.color == NodeState.WHITE:
                self.dfs_visit(self.head.data)

    def dfs_visit(self, node):
        self.time = self.time + 1
        self.head = self.createNode(node)
        self.head.data = node
        self.stack.push(self.head.data)
        self.head.startTime = self.time
        self.head.color = NodeState.GRAY
        while not self.stack.isEmpty():
            self.stack.PrintStack()
            currentVertex = self.stack.pop()
            curr = self.adjlist[currentVertex]
            while curr:
                adjvertex = curr.data
                current = self.createNode(adjvertex)
                if current.color == NodeState.WHITE:
                    self.stack.push(current.data)
                    print("adding node <- {}\n".format(current.data), end="")
                curr = curr.next
        self.head.color = NodeState.BLACK
        self.time = self.time + 1
        self.head.finishingTime = self.time
            
            