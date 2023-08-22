import math
import sys
from collections import defaultdict

class FibHeap():
    def __init__(self, elem, priority ):
        self.nDegree = 0
        self.Mark = False
        self.right = None
        self.left = None
        self.parent = None
        self.child = None
        self.mElem = elem
        self.childlist = []
        self.priority = math.fabs(priority)

    def getEdge(self):
        return (self.mElem, self.priority)

class FibTree():
    def __init__(self):
        self.mMinimum = None
        self.treeList = []
        self.Size = len(self.treeList)
    
    #helper function to ensure that the heap property is not violated. 
    # since I am storing my circular linklist in an array, the sorting in place
    # quickly extracts min and the next min is move to the root index of the treelist.
    def smallestElem(self, arr):
        smallest = 0
        for i in range(0, len(arr)):
            if arr[i] < arr[smallest]:
                arr[smallest],arr[i] = arr[i],arr[smallest]
        return arr

    #inserts a node in the rootlist if empty, it creates a singleton tree
    #if not empty, the new node key is compare with current node key and 
    # the value of the new node is compare with the value of the current node
    # if the keys are the same and the value of the current node is less than
    # the value of the new node, the new min stays the same, else the new minimum
    # is the new node key, value.
    def insert(self, key, priority):
        priority = math.fabs(priority)
        self.checkPriority(priority)
        new_node =  FibHeap(key,priority)
        self.mMinimum = new_node  
        if self.mMinimum == None and self.Size <= 0:
            self.mMinimum = new_node
            self.mMinimum.nDegree = 0
            self.mMinimum.Mark = False
        if (new_node.mElem,new_node.priority) < (self.mMinimum.mElem ,self.mMinimum.priority):  
            self.mMinimum = new_node    
        self.treeList.append(((new_node.mElem,new_node.priority)))
        self.smallestElem(self.treeList)
        self.Size += 1
     

            
    def traverse(self, node):
        if node is None:
           node = self.mMinimum
        tree = node
        while tree is not None and (tree.right != node):
            yield tree
            tree = tree.right
        yield tree

    def printList(self):
        current = self.mMinimum
        while current is not None:
            print((self.mMinimum.mElem, self.mMinimum.priority))
            current = current.right

    def printTree(self):
        for i in range(0, len(self.treeList)):
            if self.treeList[i] <  (self.mMinimum.mElem,self.mMinimum.priority):
                self.mMinimum = self.treeList[i]
            
       
    #make sure the pririty is a float and is not None
    def checkPriority(self, priority):
        priority = float(priority)
        if math.isnan(priority):
            print(priority,"is invalid")

    #check if the heap is empty. the size of the heap is the len of the list
    def isEmpty(self):
        if len(self.treeList) == [] or self.mMinimum == None:
            print("no minimum found in treelist")
            return None

    #this operation finds the minimum node in the heap along with it's priority
    def getMin(self):
        if self.isEmpty():
            print("empty heap")
        return self.mMinimum.mElem, self.mMinimum.priority
    
    #given two sub heaps, this operation merges the two 
    #heaps, determine the new minimum node for the mergeable trees
    def fib_Union(self,lst1, lst2):
        self.new_lst = lst1 + lst2
        for i, j in self.new_lst:
            new = FibHeap(i, j)
            if new.mElem < self.mMinimum.mElem:
                self.mMinimum.mElem, self.mMinimum.priority = new.mElem, new.priority
            self.insert(new.mElem, new.priority)

    #the following procedure extracts the minimum node from the rootlist and adds it children
    # to the rootlist, if it has
    # this works by first making a root out of the minimum node children
    # and then extracting the minimum node from the rootlist while maintaining the heap property
    #the helper function consolidates ensure that each root elements merging in the rootlist
    #  have distinct degree
    def extractMin(self):
        if self.isEmpty():
            print("empty heap")
        minElem = self.mMinimum
        if minElem is not None and minElem.nDegree >= 1:
            for x, y in minElem.childlist:
                child = FibHeap(x, y)
                self.insert(child.mElem,child.priority)
                child.parent = None
                minElem.childlist.clear()
            #self.treeList.remove(minElem.mElem, minElem.priority)
            if minElem == minElem.right:
                self.mMinimum = None
                self.treeList = []
            else:
                self.mMinimum = minElem.right
                self.consolidate()
            
        self.treeList.remove((minElem.mElem, minElem.priority))
        self.Size -= 1
        return minElem.mElem,minElem.priority


    # the consolidate function reduces the number of trees in the rootlist by merging
    # trees of equal degree together. given two trees x and y in the rootlist with the same degree, 
    # if x.key <= y.key, the helper function Fib_Link will make y a child of x, thus merging Y with x.
    # this happens until only trees of distinct degree are in the rootlist.
    def consolidate(self):   
        elem = self.mMinimum
        arr = [(math.floor(self.Size)/2)]
        for elem.mElem, elem.priority in self.treeList:
            x = FibHeap(elem.mElem, elem.priority)
            d = x.nDegree
            while arr[d] != []:
                y = FibHeap(elem.mElem, elem.priority)
                arr[y.nDegree] = arr[d]
                if x.mElem > y.mElem:
                    temp = y
                    x,y = y,temp
                self.fib_Link(y, x)
                arr[d] = None
                d += 1
            arr[d] = x
        self.mMinimum.mElem,self.mMinimum.priority = None
        self.treeList.clear()
        for i in range(0, len(arr)):
            if arr[i] != []:
                if self.mMinimum.mElem == None and self.Size <= 0:
                    self.mMinimum.right = self.mMinimum.left = self.mMinimum.mElem,self.mMinimum.priority
                    self.mMinimum.mElem,self.mMinimum.priority = arr[i]
                else:
                    if arr[i] < (self.mMinimum.mElem):
                        self.mMinimum.mElem, self.mMinimum.priority = arr[i]
                        #self.treeList.insert(arr[i], 0)
                #self.treeList.append((self.mMinimum.mElem, self.mMinimum.priority))

    # given two trees of equal degree(equal amount of children), if x.key <= y.key,
    # remove y from the rootlist, make y a child of x, increment x.degree and clears the mark on y.
    def fib_Link(self, y, x):
        x = self.mMinimum
        y = self.mMinimum
        y.parent = x
        self.treeList.remove(y.mElem, y.priority)     
        x.childlist.append(y)
        x.nDegree = len(x.childlist)
        x.nDegree += 1
        self.Size -= 1
        y.Mark = False
           

            
    
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
print(fib.insert(10, 5))
print(fib.insert(1, 6))
print('value of the fibonacci heap: {}'.format(fib.treeList))
print('the minimum value of the fibonacci heap: {}'.format(fib.getMin()))
print('the minimum value remove from the rootlist of the fibonacci heap: {}'.format(fib.extractMin()))
print(fib.insert(2, 9))
#fib.printList()
print('before removing the  minimum value of the fibonacci heap: {}'.format(fib.treeList))
print('the minimum value of the fibonacci heap: {}'.format(fib.getMin()))
print('the minimum value remove from the rootlist of the fibonacci heap: {}'.format(fib.extractMin()))
print('after removing the  minimum value of the fibonacci heap: {}'.format(fib.treeList))
#print(fib.insert(8, 7))
#print(fib.fib_Union([(1,4), (9,2)], [(7,9), (6,4)]))
#print('the minimum value of the fibonacci heap: {}'.format(fib.getMin()))
#print(fib.insert(1, 5))
#print('the minimum value of the fibonacci heap: {}'.format(fib.getMin()))
#print(fib.extractMin())
#print(fib.insert(1, 2))
#print('the minimum value of the fibonacci heap: {}'.format(fib.getMin()))
#fib.printList()
#fib.printTree()
#print(fib.getMin())
#print(fib.extractMin())
#print(fib.fib_Union([(1,4), (9,2)], [(7,9), (6,4)]))
#print(fib.getMin())
#print(fib.extractMin())









