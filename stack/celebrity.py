class Node:
  def __init__(self,value):
    self.data = value
    self.next = None


class Stack:
  def __init__(self):
    self.top = None
    self.size  = 0

  def push(self,value):
    new_node = Node(value)
    new_node.next  = self.top
    self.top = new_node
    self.size = self.size+1

  def pop(self):
    if(self.top == None):
      return "Stack is  Empty"

    else:
      self.top = self.top.next
      self.size = self.size-1

  def traverse(self):
    current = self.top
    while current != None:
      print(current.data , end = "->")
      current = current.next

    return