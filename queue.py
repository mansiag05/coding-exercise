class queue:
	def __init__(self):
		self.q = []
		
	# Element is inserted at the end	
	def insert(self,val):
		self.q.insert(len(self.q),val)
	
	# Remove element from front
	def remove(self):
		if len(self.q)==0:
			return "Empty Queue!"
		else:
			return self.q.pop(0)

	def isempty(self):
		if(len(self.q)==0):
			return True
		else:
			return False
			
	# Print all the elements of the queue
	def display(self):
		if(len(self.q)==0):
			return "Empty Queue!"
		else:
			for val in self.q:
				print(val)
				
