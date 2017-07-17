```
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next  = next
```

## BINARY TREE - SEARCHES, findMIN, successor

## BFS

```
queue = [root]
level = 1

while queue:
  size = len(queue)
  for i in range(size):
    node = queue.pop(0)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
     
  level += 1

return level
```

```
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
```

## Graph BFS

```
#UGN is UndirectedGraphNode object
if node is None: return None

copyNode = UGN(node.label)
dic = {}
dic[node] = copyNode
queue = [node]

while queue:
  cur = queue.pop(0)
  
  for n in cur.neighbors:
    if n in dic:
      dic[cur].neighbour.append(dic[n])
    else:
      nCopy = UGN(n.label)
      dic[n] = nCopy
      dic[cur].neighbors.append(nCopy)
      queue.append(n)
return dic[node]
```

## Meeting
```
Given some array A:
if height is None or len(height) == 0:
    return 0
r,l = 0, len(A)-1
while l<r:
  some logic
  r += 1
  l -= 1
return something
```

## Tail - One pointer trails behind to take in values that moving pointer might need to place to front
```
if nums == None or len(nums) == 0:
    return len(nums)

tail = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[tail] = nums[i]
        tail += 1
return tail
```

## ARRAY BINARY SEARCH
```
	def binarySearch(alist, item):
2	    first = 0
3	    last = len(alist)-1
4	    found = False
5	
6	    while first<=last and not found:
7	        midpoint = (first + last)//2
8	        if alist[midpoint] == item:
9	            found = True
10	        else:
11	            if item < alist[midpoint]:
12	                last = midpoint-1
13	            else:
14	                first = midpoint+1
15	
16	    return found
```



