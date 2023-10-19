#Definig Node
class Node:
  def __init__(self,value):
    self.data = value
    self.next =  None

#creating a linked list
class Linked_list:
  def __init__(self):
    self.head = None
    self.size = 0

  def add_node_head(self,value):
    new_node = Node(value)
    new_node.next =  self.head
    self.head = new_node
    self.size += 1

  def add_node_tail(self,value):
    new_node  = Node(value)
    current = self.head
    while current.next != None:
      current = current.next

    current.next = new_node
    self.size = self.size +1

  def add_after(self,value,item):
    new_node = Node(value)
    current = self.head
    while current.data != item:
      current = current.next

    new_node.next = current.next
    current.next = new_node
    self.size = wslef.size +1

  def clear(self):
    self.head =  None
    self.size = 0

  def reverse(self):
    current = self.head
    prev = None
    while current != None:
      temp = current.next
      current.next = prev
      prev = current
      current  = temp
      self.head = current

  def traverse(self):
    current = self.head
    while current != None:
      print(current.data , end =  "->")

    return
      
def main ():
  l = Linked_list()
  l.add_node_head(23)
  l.add_node_head(21)
  l.add_node_head(2)
  l.add_node_head(200)
  l.traverse()
      
      