import ctypes

class DynamicArray:
	def __init__(self):
		self.capacity = 1
		self.length = 0
		self.arr = (ctypes.py_object * self.capacity)()

	def append(self, item):
		if self.length == self.capacity:
			new_arr = (ctypes.py_object * (2 * self.capacity))()
			for i in range(self.length):
				new_arr[i] = self.arr[i]
			self.arr = new_arr
			self.capacity *= 2
		self.arr[self.length] = item
		self.length += 1