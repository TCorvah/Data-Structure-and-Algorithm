from collections import defaultdict
import sys


class Stack():

	def __init__(self):
		self.graph = []

	def getStack(self):
		return self.graph
	
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
		
	def rev(self):
		self.graph.reverse()

mystack = Stack()		
def depthFirst(graph, src):
	mystack.push(src)
	print("initial stack", src)
	visited = set()
	visited.add(src)
	while not mystack.isEmpty():
		current = mystack.pop()
		print("popping from stack", current)
		for neighbor in range(1, len(graph)):
			print(" node neighbor", neighbor)
			if neighbor not in visited:
				visited.add(neighbor)
				mystack.push(neighbor)
	return "done"
				
	







if __name__ == "__main__":
	graph = [0, 1, 2, 7]
	x = depthFirst(graph, 0)
	print(x)
	






	







	
	
	
	

	