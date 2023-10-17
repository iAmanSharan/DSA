#Defining  a node
class Node:
  def __init__(self,value):
    self.data = value
    self.next = None

#Defining a Linked List Class
class Linked_list:
  def __init__(self):
    self.head = None
    self.n = 0
    
  def __str__(self):
    current = head
    if current == None:
      return "Empty Linked List"
    result = ""
    while current != None:
      result = result + f"{current.data}"  +"->"
      current = current.next
    return result[:-2]

  def addition_thru_head(self,value):
    new_node = Node(value)
    new_node.next = self.head
    self.head =  new_node
    self.n = self.n + 1
    
  def additin_thru_tails(self,value):
    new_node = Node(value)
    current= self.head
    while current.next != None:
      current = current.next

    current.next = new_node
    self.n = self.n + 1

  def __len__(self):
    return self.n
      
  def add_after(self,value,item):
    new_node = Node(value)
    current = self.head
    while  current.data != item:
      current  = current.next

    new_node.next = current.next
    current.next  = new_node
    self.n  = self.n + 1

  def clear(self):
    self.head = None
    self.n = 0

  #indexing
  def __getitem__(self,index):
    if index<0 or index > self.n:
      return "Index Error"

    current = self.head
    for  i  in range(index):
      current = current.next

    return current.data

  
    
    