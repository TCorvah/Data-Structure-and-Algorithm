# stack Module

def getQueue():

    """Creates and returns an empty queue"""
    return []

def isEmpty(s):
    """Returns True if stack empty, otherwise returns False."""
    if s == []:
        return True
    else:
        return False

def push(s, items):
    """ Pushes item on top of queue"""
    s.append(items)

def qsize(s):
    len(s)
    


def pop(s):
    """ Returns top of queue if queue not empty. Otherwise, returns None. """
    if isEmpty(s):
        return None
    else:
        item = s.pop(0)
        return item
    
import linear_queue
#queue items gets printed twice
myqueue =  linear_queue.getQueue()
lis = [1 , 2, 3, 4]
for item in lis:
    linear_queue.push(myqueue, item)   
    print("pushing", item, "on queue")
while not linear_queue.isEmpty(myqueue):
    item = linear_queue.pop(myqueue)
    print("popping", item, "from queue")

    

