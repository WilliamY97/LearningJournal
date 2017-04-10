# Breadth First Search

BFS style questions can be seperated into three categories of which data structures that such an operation can be
performed on: **Tree, Graph, and Arrays**

The following questions can thus be categorized into each topic:

## Tree

Template Code:

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

Leverage the Queue data structure's FIFO attribute. Start with the root in the queue and then pop it off to continue
populating the queue with the children of each node added. 

**111. Minimum Depth of Binary Tree**

**2. Binary Tree Level Order Traversal**

**3. Binary Tree Level Order Traversal II**

**4. Binary Tree Right Zigzag Level Order Traversal**

**199. Binary Tree Right Side View**

**15. Populating Next Right Pointers in Each Node**

**16. Populating Next Right Pointers in Each Node II**


## Graph
**133. Clone Graph**

**261. Graph Valid Tree**

**207. Couse Schedule**

**210. Course Schedule II**


## Array
**200. Number of Islands**

**11. Word Ladder**

**12. Word Ladder II**

**13. Surrounded Regions**

**14. Perfect Squares**

**17. Wall and Gates**