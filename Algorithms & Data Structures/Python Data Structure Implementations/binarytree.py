
class Node(object):
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

def insertNode(root,key):
	if root is None: return None
	elif key > root.val:
		if root.right: insertNode(root.right,key)
		else: root.right = Node(key)
	elif key < root.val:
		if root.left: insertNode(root.left,key)
		else: root.left = Node(key)

def inOrderSearch(root):
	if root is None: return None
	inOrderSearch(root.left)
	print root.val
	inOrderSearch(root.right)

tree = Node(5)
insertNode(tree,7)
insertNode(tree,3)
insertNode(tree,9)

inOrderSearch(tree)
