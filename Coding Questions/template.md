class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

BFS

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

Meeting
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

Tail
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
```
16	    return found
