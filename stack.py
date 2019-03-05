###################################################################################
#
#	Implementing Stack in python
#
###################################################################################

class stack:
	def __init__(self):
		self.stack = []

	# using list append method to add element
	def push(self,val):
		if val:
			self.stack.append(val)
			return True
		else:
			return False

	# peek to get the topmost value
	def peek(self):		
		if (not len(self.stack)):
			return "Empty Stack"
		return self.stack[len(self.stack) -1]

	
	# pop to remove the first element
	def pop(self):
		if(len(self.stack)) <= 0:
			return("Empty Stack!")	
		else:
			return self.stack.pop()

	# Traverse the stack
	def display(self):
		if(not len(self.stack)):
			return("Stack Empty; Nothing to display")
		for item in self.stack:
			print(item)
