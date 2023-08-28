import math
from linklist_stack import Nodes

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def Empty(self):
        if self.head == None:
            print("empty queue")
            return True
        else:
            return False
        
    def queue(self, data):
        node = Nodes(data)
        if self.Empty():
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def remove(self):
        data = self.head.data
        temp = self.head
        self.head = self.head.next
        del temp
        return data
    
    def PrintQueue(self):
        print("elements in queue\n")
        queue = self.head
        while queue:
            print("Queue -> {}\n".format(queue.data), end="")
            queue = queue.next
        print("\n")

    def getInput(self):
        """Returns the user input for the stack, exits if input is -1"""
        num = int(input('Enter values for queue input (1 - num) (-1 to quit):  '))
        while num < 1 and  num != -1:
            if num == -1:
                print("bye\n") 
                exit()
            print("invalid value") 
            num = int(input('Enter values for queue input (1 - num):  ')) 		
        return num


    def driverCode(self):
        valid = False
        while not valid:
            try:
                num = self.getInput()
                if num == -1:
                    valid = True
                else:
                    for item in range(1,num + 1):
                        self.queue(item)
                        print('pushing -> : {}'.format(item), "on queue") 
                    while not self.Empty():
                        item = self.remove()
                        print('removing <- : {}'.format(item), "from queue") 
            except ValueError as err_msg:
                print(err_msg,'\n') 





queue = Queue()
x = queue.driverCode() 
print(x)  



  