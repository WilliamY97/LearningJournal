from tree import tree

"""checks how many nodes are on a specific level of a binary tree"""

count = 0

def checknodelevel(node,level,currentlevel):

	if node == None:
		return

	if (currentlevel == level):
		count += 1

	#This just optimizes my recursion so that
	#if it passes the req level it just returns
	#as it is superfluous
	if (currentlevel > level):
		return

	checknodelevel(node.left, level, currentlevel + 1)

	checknodelevel(node.right, level, currentlevel + 1)


checknodelevel(node,level,0)



