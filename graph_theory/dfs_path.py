from enum import Enum


class NodeState(Enum):
    WHITE = 'WHITE'
    GRAY = 'GRAY'
    BLACK = 'BLACK' 
      
class DFSNodes:
    """!
    @brief [Description de la classe]


    """
    def __init__(self,data):
        """!
        @brief []

        Paramètres : 
            @param self => [description]
            @param data => [description]

        """
        self.data = data
        self.next = None
        self.parent = None
        self.startTime = int
        self.finishingTime = int
        self.color = ' '
        
        
class DFStack:
    """!
    The stack class is a wrapper class for DFS
    It uses a LIFO to check for recently added elements
    and returns it.
    """
    def __init__(self):
        """!
        @brief [Description de la fonction]

        Paramètres : 
            @param self => [description]

        """
        self.front = None 
        
    
    def isEmpty(self):      
        """Returns a boolean function of
        the status of the stack
        """
        if self.front == None:
            print("stack is empty\n")
            return True
        else:
            return False

   
    def push(self, value):
        """
            adds a new element at the top of the 
            stack 
        """      
        node = DFSNodes(value)
        node.data = value
        if self.front == None:
            node.next = None
        node.next = self.front 
        self.front = node 
              
    def pop(self):
        """ removes the most recently added element
            from the stack and returns the data 
            of the element 
        """
        if self.isEmpty():
            print("queue is empty\n")
            return None
        else:
            temp = self.front
            self.front = self.front.next
            data = temp.data   
            temp1 = None
            temp = temp1
            return data
    
    def PrintStack(self):
        """Prints staus of current vertex and list 
           elements in the stack
        """
        stack = self.front
        print("stack elements\n head", end = "")  
        while stack is not None:
            print("stack -> {}\n".format(stack.data), end="")
            stack = stack.next
        print("\n")
        
        
#A graph class using adjacency list representation. in this implementation, an undirected
# graph is being used. the graph class initialize the number of vertices, visited set and the stack class
def main(): 
     
        
    if __name__ == "__main__":
        main()  
        
    
        
        
        