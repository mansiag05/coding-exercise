from tree import Node

def levelordertraversal(node):
	#calculate height of tree
	h = node.height()
	print("height of tree is: ",h)	
	for i in range(0,h):
		print("Node at height "+ str(i) +" is: ")
		printlevelorder(node,i)


def printlevelorder (node,height):
	if (height==0):
		print(node.data)
	else:
		if(node.left is not None):
			printlevelorder(node.left,height-1)
		if node.right is not None:
			printlevelorder(node.right,height-1)
	
	
# uncomment to run level order traversal for a sample tree
'''
root = Node(15)
root.insert(10)
root.insert(5)
root.insert(2)
root.insert(3)
root.insert(9)
root.insert(30)
root.insert(35)
root.insert(20)
'''

'''
root=Node(2)
'''

levelordertraversal(root)


