import math
import sys

class FibHeap():
    def __init__(self, elem, priority ):
        self.nDegree = 0
        self.Mark = False
        self.right = self.left = self
        self.parent = None
        self.child = None
        self.mElem = elem
        self.priority = math.fabs(priority)

class FibTree():
    def __init__(self):
        self.mMinimum = None
        self.treeList = []
        self.Size = len(self.treeList)

    #inserts a node in the rootlist if empty, it creates a singleton tree
    #if not empty, the new node key is compare with current node key and 
    # the value of the new node is compare with the value of the current node
    # if the keys are the same and the value of the current node is less than
    # the value of the new node, the new min stays the same, else the new minimum
    # is the new node key, value.
    def insert(self, key, priority):
        priority = math.fabs(priority)
        self.checkPriority(priority)
        if self.mMinimum == None and self.Size <= 0:
            self.mMinimum = FibHeap(key, priority)
            self.mMinimum.mElem = key
            self.mMinimum.priority = priority
            self.mMinimum.nDegree = 0
            self.mMinimum.parent = self.mMinimum.child = None
            self.mMinimum.Mark = False
        if key < self.mMinimum.mElem and priority >  self.mMinimum.priority:   
            self.mMinimum.mElem = key
            self.mMinimum.priority = priority  
        elif key < self.mMinimum.mElem:
            key = self.mMinimum.mElem
            priority = self.mMinimum.priority
        self.treeList.append((key, priority))
        self.Size += 1
        return self.treeList
    
       
    #make sure the pririty is a float and is not None
    def checkPriority(self, priority):
        priority = float(priority)
        if math.isnan(priority):
            print(priority,"is invalid")

    #check if the heap is empty. the size of the heap is the len of the list
    def isEmpty(self):
        if self.mMinimum == None:
            return None

    #this operation finds the minimum node in the heap along with it's priority
    def getMin(self):
        if self.isEmpty():
            print("empty heap")
        return self.mMinimum.mElem, self.mMinimum.priority
    
    #given two sub heaps, this operation merges the two 
    #heaps, determine the new minimum node for the mergeable trees
    def fib_Union(self,lst1, lst2):
        self.treeList = lst1 + lst2
        print(self.treeList)
        for i,j in lst1:
            x = FibHeap(i,j) 
            x.mElem = i
            x.priority = j   
        for z,y in lst2:
            c = FibHeap(z, y)
            c.mElem = z
            c.priority = y
        if  c.mElem <  x.mElem:
            self.mMinimum = c.mElem, c.priority
            return self.mMinimum
        if c.mElem > x.mElem:
            self.mMinimum = x.mElem, x.priority
            return self.mMinimum
        print(self.treeList)
    #the following procedure extracts the minimum node from the rootlist and adds it children
    # to the rootlist, if it has
    # this works by first making a root out of the minimum node children
    # and then extracting the minimum node from the rootlist while maintaining the heap property
    #the helper function consolidates ensure that each root elements merging in the rootlist
    #  have distinct degree
    def extractMin(self):
        if self.isEmpty():
            print("empty heap")
            return
        minElem = self
        minElem.mMinimum.child = minElem.mMinimum.parent = minElem.mMinimum
        if minElem.mMinimum is not None and minElem.mMinimum.nDegree >= 1:
            for child in list(minElem.mMinimum.child):
                self.treeList.append(child)
                minElem.mMinimum.child.parent = None
                minElem.mMinimum.nDegree = 0
            self.treeList.remove((minElem.mMinimum.parent).mElem, (minElem.mMinimum.parent).priority)
            if (minElem.mMinimum.parent).mElem == self.mMinimum.mElem and self.mMinimum.priority < minElem.mMinimum.parent.priority:
                self.treeList.remove(self.mMinimum.mElem, self.mMinimum.priority)
            if minElem.mMinimum == minElem.mMinimum.right:
                self.mMinimum = None
                self.treeList.clear()
            elif self.mMinimum == minElem.mMinimum.right:
                self.consolidate()
            self.Size -= 1
            minElem.mMinimum.nDegree = 0
            minElem.mMinimum.child = None
        return minElem.mMinimum.mElem, minElem.mMinimum.priority
    
    # the consolidate function reduces the number of trees in the rootlist by merging
    # trees of equal degree together. given two trees x and y in the rootlist with the same degree, 
    # if x.key <= y.key, the helper function Fib_Link will make y a child of x, thus merging Y with x.
    # this happens until only trees of distinct degree are in the rootlist.
    def consolidate(self):   
        elem = self
        arr = [None] * elem.mMinimum.nDegree
        for elem.mMinimum.mElem, elem.mMinimum.priority in self.treeList:
            x = FibHeap(elem.mMinimum.mElem, elem.mMinimum.priority)
            d = x.nDegree
            while arr[d] != []:
                y = FibHeap(elem.mMinimum.mElem, elem.mMinimum.priority)
                if arr[y.nDegree] == arr[d]:
                    if x.mElem > y.mElem:
                        self.fib_Link(x,y)
                    self.fib_Link(y, x)
                    arr[d] = None
                    d += 1
            arr[d] = x
        self.mMinimum.mElem = None
        self.treeList.clear()
        for i in range(0, self.Size):
            if arr[i] != []:
                if self.mMinimum.mElem == None and self.Size <= 0:
                    self.mMinimum.right = self.mMinimum.left = self.mMinimum.mElem
                    self.mMinimum.mElem, self.mMinimum.priority = arr[i]
                    self.treeList.append((self.mMinimum.mElem, self.mMinimum.priority))
                else:
                    if arr[i] < (self.mMinimum.mElem,self.mMinimum.priority):
                        self.mMinimum.mElem, self.mMinimum.priority = arr[i]
                        self.treeList.append((self.mMinimum.mElem, self.mMinimum.priority))

    # given two trees of equal degree(equal amount of children), if x.key <= y.key,
    # remove y from the rootlist, make y a child of x, increment x.degree and clears the mark on y.
    def fib_Link(self, y, x):
        x = self
        y = self
        y.mMinimum.child = None
        y.mMinimum.nDegree = 0
        y.mMinimum.parent = x
        if y.mMinimum.priority < x.mMinimum.priority:
           x.mMinimum.priority = y.mMinimum.priority
        p = self.treeList.remove(y.mMinimum.mElem, y.mMinimum.priority)
        x_list = []
        x_list.append(p)
        x.mMinimum.nDegree += 1
        self.Size -= 1
        y.mMinimum.Mark = False
           

            
    
    #the following function decrease key ensures that the new  key to be
    #inserted is less than the current key, otherwise an exception is thrown.
    # if the node who key is to be decrease is a root and it has parent with key
    # greater than the node, then min-heap order is violated and that node is cut from 
    # it's parent, else the node and key is save as the new minimum
    def fib_decrease(self, x, key):
        x = self
        x.mMinimum.mElem = x.mMinimum.parent = self  
        if key > x.mMinimum.mElem:
            print("new key is greater than current")
        x.mMinimum.mElem = key
        y = x.mMinimum.parent
        if y is not None and x.mMinimum.mElem < y.mMinimum.mElem:
            self.cut(x,y)
            self.cascadingCut(y)
        if x.mMinimum.mElem < self.mMinimum.mElem and self.mMinimum.priority < y.mMinimum.priority:
            #unpack tuples
            self.mMinimum = x.mMinimum.mElem, x.mMinimum.priority

    # this function removes node from the  childlist of y
    # decrementing y degree and adding node to the rootlist.
    # this is a helper function for decrease key as in the case where y is a 
    # parent of node but y key is greater than node, which violates min-heap
    def cut(self, x, y):
        x = self.mMinimum
        y = self.mMinimum
        y.child = x
        for child in list(y.child):
            d = list.remove(child)
            self.treeList.append(d)
        x.parent = None
        x.Mark = False

    def cascadingCut(self, y):
        y = self.mMinimum
        z = y.parent
        if z is not None:
            if y.Mark == False:
                y.Mark = True
            else:
                self.cut(y, z)
                self.cascadingCut(z)

    def delete(self, x):
        x = self.mMinimum
        self.fib_decrease(x, math.inf("inf") )
        self.extractMin()
    




       


                
                

        







fib = FibTree()
#print(fib.insert(1, 5))
#print(fib.insert(10, 5))
#print(fib.insert(1, 6))
#print(fib.insert(2, 9))
#print(fib.insert(8, 7))
print(fib.fib_Union([(7,4), (9,2)], [(7,9), (6,4)]))





