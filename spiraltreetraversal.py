from tree import Node

def spiraltraversal(node):
	h = node.height()
	print("Tree has " + str(h) + " height")
	flag = True
	for i in range(0,h):
		flag = not flag
		level_print(node,i,flag)

def level_print(node,h,flag):
	if h==0:
		print(node.data)
	elif flag ==True:
		if(node.left is not None):
			level_print(node.left,h-1,flag)
		if(node.right is not None):
			level_print(node.right,h-1,flag)
	elif flag==False:
		if(node.right is not None):
			level_print(node.right,h-1,flag)
		if(node.left is not None):
			level_print(node.left,h-1,flag)


#uncomment to try a sample spiral tree traversal

'''
Structure of tree that we are creating below

          15
        /    \
      10      30
     /      /    \ 
    5      20     35
  /   \         /   \
 2     9      33     50
  \                    \ 
   3                    60
                          \ 
                           100    

Spiral Tree Traversal: 15 10 30 35 20 5 2 9 33 50 60 3 100

'''	


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
root.insert(50)
root.insert(33)
root.insert(60)
root.insert(100)
spiraltraversal(root)
'''
