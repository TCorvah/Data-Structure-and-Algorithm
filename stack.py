from collections import defaultdict
import sys


class Stack():

	def __init__(self):
		self.graph = []
	
	def isEmpty(self):
		if self.graph == []:
			print("stack is empty")
			return True			
		else:
			return False
		
	def top(self):
		if self.isEmpty():
			print("stack is empty")
		else:
			return self.graph[len(self.graph - 1)]
		
	def push(self, item):
		self.graph.append(item)

	def pop(self):
		if self.isEmpty():
			print("empty stack")
		else:		
			item = self.graph.pop()		
			return item
		

mystack = Stack()		
def LiFo(graph):
	visited = set()
	src = graph[0]
	visited.add(src)
	mystack.push(src)
	print("initial element on stack", src)
	while not mystack.isEmpty():
		for neighbor in graph:
			if neighbor not in visited:
				visited.add(neighbor)
				mystack.push(neighbor)
				print(" pushing on stack", neighbor)
		current = mystack.pop()
		print("popping from stack", current)
	return "done"
				

if __name__ == "__main__":
	graph = [0, 1, 2, 7]
	x = LiFo(graph)
	print(x)
	






	







	
	
	
	

	