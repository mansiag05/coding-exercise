class Node:
	def __init__(self,val):
		self.data = val
		self.left = None
		self.right = None

	# if value of node is smaller than root node, insert in the left tree
	# if value of node is greater than root node, insert in the right tree
	def insert(self, val):
		if self.data:
			if val < self.data:
				if self.left is None:
					self.left = Node(val)	
				else:
					self.left.insert(val)
			else:
				if self.right is None:
					self.right = Node(val)
				else:
					self.right.insert(val)
		else:
			self.data = val

	# inorder traversal of tree 
	def in_printtree(self):
		if self.left:
			self.left.in_printtree()
		print(self.data)
		if self.right:
			self.right.in_printtree()

	# pre-order traversal of tree
	def pre_printtree(self):
		if self.data:
			print(self.data)
		if self.left:
			self.left.pre_printtree()
		if self.right:
			self.right.pre_printtree()

	# post order traversal of tree
	def post_printtree(self):
		if self.left:
			self.left.post_printtree()
		if self.right:
			self.right.post_printtree()
		if self.data:
			print(self.data)


	def search(self,key):
		if(self.data == key):
			return True
		elif(key < self.data and self.left is not None):
			return self.left.search(key)	
		elif(key >= self.data and self.right is not None):
			return self.right.search(key)

		return False
	
	
