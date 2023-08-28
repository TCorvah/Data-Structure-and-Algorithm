
class Node():
    def __init__(self,key):    
        self.parent = None
        self.child = None
        self.left = None
        self.right = None
        self.key = key
        self.g = 0
        self.h = 0
        self.f = 0
       
    