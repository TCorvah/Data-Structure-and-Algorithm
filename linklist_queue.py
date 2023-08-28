import math

#a node class to insert data into the queue
class Nodes:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
#implementation of the queue data structure, 
class Queue:
    def __init__(self) -> None:
        self.head = None


    def Empty(self):
        """Returns true if queue is empty, otherwise returns False"""
        if self.head == None:
            print("empty queue")
            return True
        else:
            return False
        
    def enQueue(self, data):
        """Add items  in the queue, if the queue is empty, the added item is the 
            head and tail of the queue, else the newly added item go to the right 
            of the queue
        """
        node = Nodes(data)
        if self.Empty():
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def deQueue(self):
        """Removes item from the front of the queue. the next item in the
            queue becomes the front of the queue until the queue is empty
        """
        data = self.head.data
        temp = self.head
        self.head = self.head.next
        temp1 = None
        temp = temp1
        return data
    
    def PrintQueue(self):
        """Prints the queue as the item gets added, shows the queue after an
            item has been remove from the queue
        """
        print("elements in queue\n")
        queue = self.head
        while queue:
            print("-> {}".format(queue.data), end="->")
            queue = queue.next
        print("\n")

    def getInput(self):
        """Returns the user input for the queue, exits if input is -1"""
        num = int(input('Enter values for queue input (1 - num) (-1 to quit):  '))
        while num < 1 and  num != -1:
            if num == -1:
                print("bye\n") 
                exit()
            print("invalid value") 
            num = int(input('Enter values for queue input (1 - num):  ')) 		
        return num


    def driverCode(self):
        """checks user input if valid and add/removes items in the queue
            user quits on -1 or keep on using the program, if invalid input
            is entered, user is prompted to enter valid numeric integers
        """
        valid = False
        while not valid:
            try:
                num = self.getInput()
                if num == -1:
                    valid = True
                else:
                    for item in range(1,num + 1):
                        self.enQueue(item)
                        self.PrintQueue()
                    while not self.Empty():
                        item = self.deQueue()
                        print("removing items from queue\n")
                        print("<- {}".format(item), end="<-")
                        print()
                        self.PrintQueue()                       
            except ValueError as err_msg:
                print(err_msg,'\n') 





queue = Queue()
x = queue.driverCode() 
print(x)  



  