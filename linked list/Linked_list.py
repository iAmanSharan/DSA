class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Linked_List:
  def __init__(self):
    self.size = 0
    self.head = None
    self.tail = None

  def add_node_begin(self,data):
    new_node = Node(data)
    if self.size == 0:
      self.head = new_node
      self.tail = new_node
      self.size += 1
    else:
      new_node.next = self.head
      self.head = new_node
      self.size += 1

  def getsize(self):
    return self.size

  def show(self):
    current = self.head
    llist = ""
    while current != None:
      llist = llist + f"{current.data}" + "->"
      current = current.next
    return llist[:-2]

  def add_node_behind(self,data):
    new_node = Node(data)
    if self.size == 0:
      self.head = new_node
      self.tail = new_node
      self.size +=1
    else:
      self.tail.next = new_node
      self.tail = new_node
      self.size += 1

  def delete_node_begin(self):
    if self.size != 0:
      self.head = self.head.next
      self.size -= 1
    else:
      print("Action not possible")

  def delete_note_end(self):
    if self.size != 0:
      current = self.head
      while current.next.next != None:
        current = current.next
      current.next = None
    else:
      print("Action not possible")
  
  def add_node_after(self,data, item):
    current = self.head
    while current != None:
      if current.data == item:
        new_node = Node(data)
        temp = current.next
        current.next = new_node
        new_node.next = temp
        return self.show() 
      current = current.next
    return "Item not found"     
  
  def add_node_position(self,data, position):
    if position > self.size:
      return "Position invalid"
    new_node = Node(data)
    current = self.head
    count =1
    while current != None:
      if count == position-1:
        temp = current.next
        current.next = new_node
        new_node.next = temp
        return self.show()
      current = current.next
      count = count +1

  def delete_node_position(self,position):
    count = 1
    current = self.head
    while current != None:
      if count == position-1:
        current.next = current.next.next
        return self.show()
      current = current.next
      count = count +1      

  def getitem(self,position):
    while True:
      if 1<= position <= self.size:
        break
    count = 1
    current = self.head
    while current != None:
      if count == position:
        return current.data
      count = count+1
      current = current.next  
  
    
    