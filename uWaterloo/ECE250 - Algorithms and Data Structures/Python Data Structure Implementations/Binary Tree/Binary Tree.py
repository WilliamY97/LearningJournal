
class Node(object):

	count = 0

	@classmethod
	def increaseCount (cls):
		cls.count = cls.count + 1

	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None
		self.increaseCount()

def insertNode(root,key):
	if root is None: return None
	elif key > root.val:
		if root.right: insertNode(root.right,key)
		else: root.right = Node(key)
	elif key < root.val:
		if root.left: insertNode(root.left,key)
		else: root.left = Node(key)

def deleteNode(root,key):
	if root is None: return None

def height(root):
	if root is None: return 0
	else: return max(height(root.left),height(root.right)) + 1

def binarySearch(root,key):
	if root is None:
		print "Nothing Found."
		return None
	if root.val == key:
		print root.val
		return root
	elif key > root.val:
		binarySearch(root.right,key)
	else:
		binarySearch(root.left,key)

def inOrderSearch(root):
	if root is None: return None
	inOrderSearch(root.left)
	print root.val
	inOrderSearch(root.right)

def preOrderSearch(root):
    if root is None: return None
    print root.val
    preOrderSearch(root.left)
    preOrderSearch(root.right)

def postOrderSearch(root):
    if root is None: return None
    postOrderSearch(root.left)
    postOrderSearch(root.right)
    print root.val,

def findMin(node):
	while node.left is not None: node = node.left
	return node

def successor(node):
	if node is None: return None
	print findMin(node.right).val

tree = Node(5)
insertNode(tree,7)
insertNode(tree,3)
insertNode(tree,8)
insertNode(tree,9)

print "How Many Nodes..."
print Node.count

print "Performing Binary Search..."
binarySearch(tree,9)

print "Performing In Order Search..."
inOrderSearch(tree)

print "Performing Pre Order Search..."
preOrderSearch(tree)

print "Performing Successor..."
successor(tree)

print "Finding Height of Tree..."
print height(tree)
