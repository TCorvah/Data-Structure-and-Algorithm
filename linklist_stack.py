import math
import sys

#This is a singly linklist implementaion of a stack
class Nodes():
	def __init__(self,data):
		self.data = data
		self.next = None

#The stack implementation consist of various functions
#initially, the head of the stack is empty, as param head == None
#a count parameter is added to keep track of stack counts. Not really needed
class Stacks():
	def __init__(self):
		self.head = None
		self.count = 0
	
	def isEmpty(self):
		""" Returns True if stack is empty, otherwise returns False"""
		if self.head == None:
			print("empty stack")
			return True
		else:
			return False
		
	
	def push(self, item):
		"""Pushes item on the top of the stack"""
		if self.isEmpty():
			self.head = Nodes(item)
		else:
			new_node = Nodes(item)
			new_node.next = self.head
			self.head = new_node
			self.count += 1  		
		
	def top(self):
		"""Returns value of the top item of stack, if stack not empty.
			Otherwise, retuns None
		"""
		if self.isEmpty():
			print("stack is empty")
		else:
			temp = self.head.next
			self.count -= 1 
			return temp	

	def pop(self):
		"""Returns top of stack if stack is empty, otherwise returns None"""
		curr = self.head
		if curr == None:
			print("empty stack")
		while curr is not None:                       
			temp = self.head.data             
			self.head = self.head.next
			curr.next  = None
			self.count -= 1  
			return temp
		
	def getInput(self):
		"""Returns the user input for the stack, exits if input is -1"""
		num = int(input('Enter values for stack input (1 - num) (-1 to quit):  '))
		while num < 1 and  num != -1:
			if num == -1:
				print("bye\n") 
				exit()
			print("invalid value") 
			num = int(input('Enter values for stack input (1 - num):  ')) 		
		return num
	

#This driver code function creates and returns a new empty stack
# an error check is included so that only valid inputs are enter for the stack
def linkStack():
	head = Stacks()
	valid = False
	while not valid:
		try:
			num = head.getInput()
			if num == -1:
				valid = True
			else:
				for item in range(1,num + 1):
					head.push(item)
					print('pushing -> : {}'.format(item), "on stack") 
				while not head.isEmpty():
					item = head.pop()
					print('popping <- : {}'.format(item), "from stack") 
		except ValueError as err_msg:
			print(err_msg,'\n') 



    

x = linkStack()
print(x)
	

	
	






	







	
	
	
	

	