import math
import sys

class FibonacciHeap():
    class Entry():
        def __init__(self,elem,priority):
            self.numdegree = 0
            self.isMark = False
            self.left = self.right = self
            self.parent = None
            self.child = None
            self.mElem = elem
            self.mPriority = priority
            self.treeTable = []
            self.toVisit = []

            self.Min = FibonacciHeap.Entry.mMin
            
            
        def getValue(self):
            return self.__mElem
        
        def setValue(self, value):
            self.mElem = value


        def getPriority(self):
            return self.mPriority
        
        def setPriority(self, priority):
            self.mPriority = priority
            
        
        mSize = 0
        mMin = None

        def enqueue(self, value, priority):
            self.checkPriority(priority)
            result = FibonacciHeap().Entry(value, priority)
            self.mMin = self.mergeList(self.mMin, result)
            self.mSize  += 1
            return result
        
        def IsMin(self):
            if self.isEmpty():
                print("heap is empty")
            return self.mMin
        
        
        def isEmpty(self):
            return self.mMin == None
        
        def heapSize(self):
            return self.mSize
        
        def merge(self, heapOne, heapTwo):
            result = FibonacciHeap().Entry()
            heapOne = FibonacciHeap().Entry()
            heapTwo = FibonacciHeap().Entry()
            result.mMin = self.mergeList(heapOne.mMin, heapTwo.mMin)
            result.mSize =  heapOne.mSize + heapTwo.mSize
            heapOne.mSize = heapTwo.mSize = 0
            heapOne.mMin = None
            heapTwo.mMin = None
            return result
        
        def dequeueMin(self):
            if self.isEmpty():
                print("heap is empty")
            self.mSize -= 1
            minElem = FibonacciHeap().Entry().mMin
            if self.mMin.right == self.mMin:
                self.mMin = None
            else:
                self.mMin.left.right = self.mMin.right
                self.mMin.right.left = self.mMin.left
                self.mMin = self.mMin.right
            if minElem.child is not None:     
                curr = minElem.child 
                while curr != minElem.child:
                    curr = FibonacciHeap().Entry()
                    curr.parent = None
                    curr = curr.right
            self.mMin = self.mergeList(self.mMin, minElem.child)
            if self.mMin == None:
                return minElem
            curr = FibonacciHeap().Entry().mMin
            for i in range(curr, len(self.toVisit)):
                if len(self.toVisit) <= 0 or self.toVisit.index(0) != curr:
                    curr  = curr.right
                self.toVisit.append(curr)
            for curr in self.toVisit:
                while True:
                    while curr.numdegree >= len(self.treeTable):
                        self.treeTable.append(None)
                    if self.treeTable.index(curr.numdegree) == None:
                        self.treeTable.insert(curr.numdegree, curr.mMin)
                        break
                    
                    other = FibonacciHeap().Entry()
                    self.treeTable.index(curr.numdegree)
                    self.treeTable.insert(curr.numdegree, None)
                    max = FibonacciHeap().Entry().treeTable
                    min = FibonacciHeap().Entry().treeTable

                    if other.mPriority < self.mMin.mPriority:
                        min = other
                        max = self.mMin
                    elif other.mPriority > self.mMin.mPriority:
                        max = other
                        min = self.mMin

                    max.right.left = max.left
                    max.left.right = max.right
                    max.right = max.left = max
                    min.child = self.mergeList(min.child, max)
                    max.parent = min
                    max.isMark = False
                    min.numdegree += 1
                    curr = min
                if curr.mMin.mPriority < self.mMin.mPriority:
                        self.mMin = curr

                return minElem
            
        def decreaseKey(self, entry, newPriority):
            entry = FibonacciHeap().Entry()
            self.checkPriority(newPriority)
            if newPriority > entry.mPriority:
                print("new priority exceeds old")
            self.decreaseKeyUnchecked(entry, newPriority)

        def delete(self, entry):
            self.decreaseKeyUnchecked(entry, float(0.0))
            self.dequeueMin()

        def checkPriority(self, priority):
            if not float.is_integer(priority):
                print(priority,"is invalid")


        def mergeList(self, one, two):
            one = FibonacciHeap().Entry()
            two = FibonacciHeap().Entry()
            if one == None and two == None:
                return None
            elif one is not None and two == None:
                return one
            elif one == None and two is not None:
                return two
            else:
                oneNext = one.right
                one.right = two.right
                two.right.left = one
                two.right = oneNext
                two.right.left = two
            if one.mPriority < two.mPriority:
                return one
            else:
                return two


        def decreaseKeyUnchecked(self, entry, priority):
            entry = FibonacciHeap().Entry()
            entry.mPriority = priority
            if entry.parent is not None and entry.mPriority <= entry.parent.mPriority:
                self.cutNode(entry)
            if entry.mPriority <= self.mMin.mPriority:
                self.mMin = entry

        def cutNode(self, entry ):
            entry = FibonacciHeap().Entry()
            entry.isMark = False
            if entry.parent == None:
                return
            if entry.right != entry:
                entry.right.left = entry.left
                entry.left.right = entry.right

            if entry.parent.child == entry:
                if entry.right != entry:
                    (entry.parent).child = entry.right
                else:
                    (entry.parent).child = None


            (entry.parent).numdegree  -= 1
            entry.left = entry.right = entry
            self.mMin = self.mergeList(self.mMin, entry)
            if (entry.parent).isMark:
                self.cutNode(entry.parent)
            else:
                (entry.parent).isMark = True
            
            entry.parent = None
