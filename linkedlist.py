class Node:
	def __init__(self,val=None):
		self.val = val
		self.nextval = None

class linkedlist:
	def __init__(self):
		self.head = None

	def insertatbeg(self, val):
		node = Node(val)
		if self.head == None:
			self.head = node
		else:
			node.nextval = self.head
			self.head = node
		
	
	def insertatend(self,val):
		node = Node(val)
		if self.head == None:
			self.head = node
		else:
			temp = self.head
			while(temp.nextval != None):
				temp = temp.nextval
			temp.nextval = node


	def deleteatbeg(self):
		if(not self.head == None):
			temp = self.head
			if(self.head.nextval == None):
				self.head = None
			else:	
				self.head = self.head.nextval
			return temp.val
		else:
			return "Empty Linked List"		

	def deleteatend(self):
		if(not self.head == None):
			temp = self.head
			if temp.nextval == None:
				head = None
				return temp.val
			while(temp.nextval.nextval != None):
				temp = temp.nextval

			ptr = temp.nextval
			temp.nextval = None
			return ptr.val
		else:
			return "Empty Linked List"

	def printlist(self):
		if(not self.head==None):
			temp = self.head
			while(temp!=None):
				print(temp.val)
				temp = temp.nextval
		else:
			return "No LinkedList!"
