# stack Module

class Queue():
    def __init__(self):
        self.queue = []
	
    def isEmpty(self):
        if self.queue == []:
            print("queue is empty")
            return True			
        else:
            return False
    
    def top(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        else:
            return self.queue[len(self.queue)]

    def add_queue(self, items):
        """ Pushes item on top of queue"""
        self.queue.append(items)

    def pops(self):
        """ Returns top of queue if queue not empty. Otherwise, returns None. """
        if self.isEmpty():
            return None
        else:
            item = self.queue.pop(0)
            return item
myqueue = Queue()	
def FiFo(graph):
    src = graph[0]
    visited = set()
    visited.add(src)
    myqueue.add_queue(src)
    print("initial element on queue", src)
    while not myqueue.isEmpty():
        for neighbor in graph:
            if neighbor not in visited:
                visited.add(neighbor)
                myqueue.add_queue(neighbor)
                print(" adding items on queue", neighbor)
        current = myqueue.pops()
        print("removing items from queue", current)
    return "done"  

if __name__ == "__main__":
	queue= [0, 1, 2, 7]
	x = FiFo(queue)
	print(x)
	
  
   

    

