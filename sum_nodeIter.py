class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None

class LinkList:
    def __init__(self, ):
        self.head = None
        sum_list = []
    
    def add_n(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        n_list = sum(nodes)
        return n_list
    
    def print(self,head):
        val = 0
        head = self.head
        while head is not None:
            val += head.data            
            head = head.next
        return val
    
        
      
#print("\ninitial list operation for sum")  
llist = LinkList()
#user_input = input("Enter first and second numbers to add:  ")
#num1, num2 = tuple(int(item) for item in user_input.split())
#print(llist.sum_n(num1,num2))
llist.head = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)


llist.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
#v  = llist.add_n()
v =llist.print(llist.head)
print(v)
