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

**Solution:** To find the minimum depth of a binary tree we need to find the most shallow node. A shallow node is one defined
to have no children. To do this we can perform a BFS on the tree and when we find a node without children we return the
level we're on. If we don't find anything we can simply return the level we're on once we finish the BFS aka lowest level.

**102. Binary Tree Level Order Traversal**

Template Code For Level Order
```
queue = [root]

while queue:
  size = len(queue)
  for i in range(size):
    node = queue.pop(0)
    if node.left: queue add left
    if node.right: queue add right
    level.append(node.val)
  res.append(level)
return res
```
Key to this question is to store the value of the nodes in a complete set of the for loop to a temporary list. Then
afterwards append that list to a res. This works naturally as the nodes from a set of the for loop are the nodes of
a level.

**107. Binary Tree Level Order Traversal II**

Same as previous question but insert the level of values into the result from the front. This might make it O(n^2) so
doing a rotation might make it faster.

**103. Binary Tree Right Zigzag Level Order Traversal**

Have a flag that identifies whether or not the level list needs to be reversed or not and then append it to the result

**199. Binary Tree Right Side View**

The strategy here is to add new nodes to the queue from right to left. Then we only add to the result when the length of the result
is equal to the level we're on. This allows the first node of every level to be added to the result - good in the case that the rightmost node is missing.

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
