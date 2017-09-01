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

**116. Populating Next Right Pointers in Each Node**

The question here really is to generate a linked list from each level of a PERFECT binary tree. To do this we have a variable that holds
the previous node and when we go to the next node we can set that last nodes pointer to point to the current one. At the end of the
level the last node will simply be set to point to None.

**117. Populating Next Right Pointers in Each Node II**

By using level order traversal, it is the same strategy as 116. even when it's incomplete tree.

## Graph

The first three questions are graph-based whereas the last three are topological sorts

The Template Code for Graph based BFS requires a dictionary to track what has been visited already:

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

**133. Clone Graph**

Simply re-creating the graph in this question. A BFS will help track down all the nodes and then store them into a dictionary and
also update current nodes neighbors to have it. If a neighbor already exists in the dictionary then we simply need to update the 
current nodes neighbours to have it. The purpose of the dictionary is to know which nodes have been visited (thus what to enqueue).

**261. Graph Valid Tree**

This question asks to check if a graph is a valid tree. So in a tree there must be n-1 edges (one edge case). We take the edges
given to us and populate the neighbors of each node with the corresponding node they are connected to. Then we go through the nodes
and pop their neighbors into the queue. If by the end of it the neighbors dict is not empty - then there is a node that's not connected
and therefore it's not a tree - otherwise it is.

NOTE: The extend() method does this [1,2,3].extend([4,5]) -> [1,2,3,4,5]
Pop(a,b) is used on a dict and the b value is the default return value if a isn't found

**323. Number of Connected Components in an Undirected Graph**

First, set up a dictionary that holds the neighbours of the nodes in the graph and populate it from edges. Then we define a visited
variable that keeps track of nodes already visited before - if they have then they were in a component we've seen already before and do
not need to be BFS'd - also implement a res = 0. After we iterate through the nodes and see if they have been visited - if not then
we mark it visited and increase result (there is a component). We initialize a queue with the i'th node in it and perform a BFS on it.
If the neighbor has not been visited then add it to the queue and mark it as visited. This BFS will essentially expose all nodes that
are part of the component and mark them as visited so they are not checked again when iterating through all nodes.

**TOPOLOGICAL SORT BASED QUESTIONS**

**207. Course Schedule**

A topological sort can be performed by keeping track of the in-degrees of a graph. Set up a dictionary that keeps track of the
nodes and which ones they connect to. While doing this you can populate an array that keeps track of how many in degrees there are
to a particular node. Finally iterate through your indegree array and find the nodes that have zero in-degree. Add these to a zero
array which you will pop nodes from and check the nodes they connect to. Subtract an in degree for each connected node and then
check if it now has zero in-degrees. If so then add it to the queue of zero in-degree nodes to be checked. At the end, delete the node we initially popped from the graph hash. When there are no more nodes in the zero array, we check if the length of the graph dict is
zero - if it is then we know there are no contradictary cycles in the graph and based off the pre-reqs this course schedule can be
complete.

**210. Course Schedule II**

**310. Minimum Height Trees**

## Array

Array based BFS is similar to Graphs in that we need to be concerned if we have visited a certain node before. In this case we don't
have a neighbours dictionary as the graph would have or children like a tree would. We instead check the adjacent array slots to the
array slot we are currently on and see if they have been visited or not. If not we mark it as visited and put it into the queue.

```
res = []
queue = [[a,b]]

while queue:
    if [a,b] not visited:
      [a,b] = queue.pop(0)
      grid[a,b] = visited
      res.append([a,b])
      if [a,b] right up down left node isn't visited
      go and put them into queue
```
```
       m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        
        res = 0
        queue = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append([i,j])
                    grid[i][j] = '0'
                    while queue:
                        [a,b] = queue.pop(0)

                        if a+1 < m and grid[a+1][b] == '1':
                            queue.append([a+1,b])
                            grid[a+1][b] = '0'
                        
                        if b+1 < n and grid[a][b+1] == '1':
                            queue.append([a,b+1])
                            grid[a][b+1] = '0'                        
                        
                        if a-1 >= 0 and grid[a-1][b] == '1':
                            queue.append([a-1,b])
                            grid[a-1][b] = '0'
                            
                        if b-1 >= 0 and grid[a][b-1] == '1':
                            queue.append([a,b-1])
                            grid[a][b-1] = '0'
                    res += 1
        return res
```

**200. Number of Islands**

Traverse through grid and if you find an island with '1' then go and do a BFS on it to find the entirety of that island and mark them as
0's. Once you're done and there is no more nodes in the queue add 1 to result and keep going through grid to find more islands with 1 and doing BFS's on them.

**11. Word Ladder**

**12. Word Ladder II**

**13. Surrounded Regions**

**14. Perfect Squares**

**17. Wall and Gates**
