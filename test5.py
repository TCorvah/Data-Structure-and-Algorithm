class Matrix(object):
    def __init__(self, vertices):
        self.adjMatrix = []
        for i in range(vertices):
            self.adjMatrix.append([0 for i in range(vertices)])
        self.numVertices = vertices
        

    def addEdge(self, v1, v2, cost):
        if v1 == v2:
            print("same vertex %d and %d" %(v1, v2))
        self.adjMatrix[v1].append(tuple((v2, cost)))
        self.adjMatrix[v2].append(tuple((v1, cost)))

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.numVertices


    def printMatrix(self):
        for row in self.adjMatrix:
           for j in row:
            print(row, j)
            print()
def main():

   g = Matrix(5)
   g.addEdge(0, 1, 5)
   g.addEdge(0, 2, 4)
   g.addEdge(1, 2, 8)
   g.addEdge(2, 0, 5)
   g.addEdge(2, 3, 4)

   g.printMatrix()



if __name__ == '__main__':
    main()



def aStar(self, node, startNode, endNode):
        openlist = []
        openlist.append(startNode)
        visted = set()
        traverseNodes = 0
        traverseNodes += 1    
        startNode = nodes.Node(0)
        startNode.g = 0
        startNode.h = self.heuristics(nodes.Node(startNode), nodes.Node(endNode))
        startNode.f = startNode.g + startNode.h
        while len(openlist) > 0:
           current_index =  self.getNextIndex(openlist)
           current_node = openlist[current_index]
           if current_node == endNode:
               path = []
               aNode = nodes.Node(current_node)
               while aNode.parent is not None:
                   path.append(aNode.key)
                   aNode = aNode.right
               path.append(startNode)
               return {path: path, traverseNodes : traverseNodes }      
        openlist.remove(current_index)
        visted.add(current_node)
        traverseNodes += 1  
        neighbors = self.getNeighbor(current_node, node)
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor in visted:
                continue
            tentative_g = current_node.g + self.euclidean(current_node, neighbor)
            tentativeIsBetter = False
            if neighbor not in openlist:
                neighbor.h = self.heuristics(neighbor, endNode)
                openlist.append(neighbor)
                tentativeIsBetter = True
            elif tentative_g < neighbor.g:
                 tentativeIsBetter = True
            else:
                tentativeIsBetter = False
            if tentativeIsBetter:
                 neighbor = nodes.Node(current_node)
                 neighbor.left = neighbor.right
                 neighbor.g = tentative_g
                 neighbor.f = neighbor.g + neighbor.h
            return {path: [], traverseNodes: traverseNodes}






class FibHeap():
    def __init__(self):
        self.minimum = None
        self.nodecount = 0
        self.nodefound = False
        self.rootlist = []
        self.childlist = []

        
    def insert(self,value, priority):
        if self.minimum is None:
           self.minimum = FibTree(value,priority)
           self.right = self.left = self.minimum
           self.rootlist.append((self.minimum.data, self.minimum.priority))
        if self.minimum is not None and value < self.minimum.data:
           nodes = FibTree(value, priority)
           self.minimum = nodes
        self.nodecount += 1
        return self.rootlist
    
    def isMin(self):
        if self.minimum is None:
           return None
        node = FibTree(self.minimum.data, self.minimum.priority)
        return node.data, node.priority
    
    def isEmpty(self):
        return self.minimum == None
    
    def union(self, root1, root2):
        root1 = self.minimum
        root2 = self.minimum  
        if (root1 == None) or (root2 is not None and root2.data < root1.data):
            self.minimum = root2
        self.nodecount = root1.size + root2.size
        return self
    
    def merge(self, one, two):
        res = self
        one = self
        two = self
        res.minimum = self.mergelist(one.minimum, two.minimum)
        one.nodecount = two.nodecount = 0
        one.minimum = None
        two.minimum = None
        return res
    

    def mergelist(self, one, two):
        result = FibTree(0, 0.0)
        last = result
        while True:
           if one is None:
              last.right.left = two
              break
           if two is None:
              last.right.left = one
              break
           one = self.minimum
           two = self.minimum
           if one.data <= two.data:
               last.right = one.right
               last.left = one
               one.right.left = last
           else:
               last.right = two.right
               last.left = two
               one.right.left = last
           last = last.right.left
        return result
        

               
    
    def traverse(self, node):
        if node is None:
           node = self.minimum
        tree = node
        while tree is not None and (tree.right != node):
            yield tree
            tree = tree.right
        yield tree
    
    def extract_min(self):
        min_node = self.minimum 
        if min_node is not None:           
            if min_node.child is not None:
                curr = self.traverse(min_node.child)
                self.rootlist.append(curr)
            self.rootlist.remove(min_node)    
            if min_node == min_node.right:
                    self.minimum = None
            else:
                self.minimum == min_node.right
                self.consolidate()
            self.nodecount -= 1
        return min_node.data, min_node.priority
    
     
    def consolidate(self):
        pass
                
                

    def enqueue(self):
        if self.isEmpty():
            print("heap underflow\n")
        self.nodecount -= 1
        min_elem = self.minimum
        if min_elem.right == self.minimum:
            self.minimum = None
        else:
            (self.minimum.left).right = self.minimum.right
            (self.minimum.right).left = self.minimum.left
            self.minimum = self.minimum.right
        if min_elem.child != None:
            curr = FibTree(min_elem.data, min_elem.priority)
            curr.parent = None
            while curr != min_elem.child:
                curr = curr.right
        self.minimum = self.union(self.minimum,min_elem.child )
        if self.minimum == None:
            return min_elem
        visit = []
        curr = self.minimum
        if visit.index(0) != curr:
            curr = curr.right
        visit.append(curr)

            

    def fibLink(self, y, x): 
        y = self     
        self.rootlist.remove(y)
        (y.left).right = y
        


    def fibHeap(self, data, value):
        nodes = FibTree(data, value)
        if data > nodes.data:
            print("new key is greater than current key\n")
        nodes.data = data
        y = nodes
        if y.parent is not None and nodes.data < y.data:
            self.cut(data, y)

             
    def cut(self, x, y):
        y = self.minimum
        y.child = x
        self.childlist.remove(y.child)
        y.numdegree -= 1
        x = self.minimum
        self.rootlist.append(y.child)
        x.parent = None
        x.mark = False


    def  cascadingCut(self, y):
         if y is None:
            y = self.minimum
         z = y.parent
         if z is not None:
             if y.mark is False:
                 y.mark = True
             else:
                 self.cut(y, z)
                 self.cascadingCut(self,z)


def main():
    heap = FibHeap()
    heap.insert(7, 12)
    heap.insert(3, 10)

    print('the minimum value of the fibonacci heap: {}'.format(heap.isMin()))            

if __name__ == "__main__":
    main()       
  
      

    
   
        


      

        
