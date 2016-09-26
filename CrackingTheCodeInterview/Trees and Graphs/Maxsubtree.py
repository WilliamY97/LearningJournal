from tree import tree
import math

"""Check for maximum sub tree within a binary search tree"""

"""If it were a general graph then instead of checking just the
left and right nodes you need to iterate through the children of a node,
call maxsubtree on them and then add them to the node's maxvalue"""

def maxsubtree (node):
	maximum = -inf

	if (node.left == None && node.right == None):
		node.maxvalue = node.value

	elif (node.left == none):
		maxsubtree(node.right)
		node.maxvalue = node.value + node.right.maxvalue 
	
	elif (node.right == none):
		maxsubtree(node.left)
		node.maxvalue = node.value + node.left.maxvalue

	else:
		maxsubtree(node.right)
		maxsubtree(node.left)
		node.maxvalue = node.value + node.left.maxvalue + node.right.maxvalue

	if node.maxvalue > maximum:
		maximum = node.maxvalue

	return maximum 