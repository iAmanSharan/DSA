class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node_begin(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size +=1             
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1  
    
    def add_node_end(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size = self.size+1              
