class Node:
  def __init__(self,value):
    self.data = value
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self,value):
    new_node = Node(value)
    if self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def dequeue(self):
    self.head = self.head.next

  def traverse(self):
    current = self.head
    while current !=None:
      print(current.data, end = "->")
      current = current.next

    return

def main():
  q = Queue()
  q.enqueue(23)
  q.enqueue(12)
  q.enqueue(97)
  q.dequeue()
  q.traverse()

main()
