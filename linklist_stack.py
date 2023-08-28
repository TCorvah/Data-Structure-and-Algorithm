import math
import sys

class Nodes():
	def __init__(self,data):
		self.data = data
		self.next = None


class Stacks():
	def __init__(self):
		self.head = None
		self.count = 0
	
	
	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False
		
	
	def push(self, item):
		if self.isEmpty():
			self.head = Nodes(item)
		else:
			new_node = Nodes(item)
			new_node.next = self.head
			self.head = new_node
			self.count += 1  		
		
	def top(self):
		if self.isEmpty():
			print("stack is empty")
		else:
			return self.head	

	def pop(self):
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
		num = int(input('Enter values for stack input (1 - num) (-1 to quit):  '))
        #added one as the range function counts up to but not including the last element
		while num < 1 and  num != -1:
			if num == -1:
				print("bye\n") 
				exit()
			print("invalid value") 
			num = int(input('Enter values for stack input (1 - num):  ')) 		
		return num
	


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
					print('popping -> : {}'.format(item), "from stack") 
		except ValueError as err_msg:
			print(err_msg,'\n') 



    

x = linkStack()
print(x)
	

	
	






	







	
	
	
	

	