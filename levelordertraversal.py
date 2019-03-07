from tree import Node
from queue import queue

def levelordertraversal(node):
	if node is None:
		return False

	else:
		q = queue()
		q.insert(node)
		while (not q.isempty()):
			temp = q.remove()	
			if(temp.left is not None):				
				q.insert(temp.left)
			if(temp.right is not None):
				q.insert(temp.right)
			print(temp.data)
			

# uncomment to run level order traversal for a sample tree
'''
root = Node(15)
root.insert(10)
root.insert(5)
root.insert(2)
root.insert(3)
root.insert(9)
levelordertraversal(root)
'''


		

