#B-Trees

![Reference Image](http://www.cs.cornell.edu/courses/cs3110/2011sp/recitations/rec24-B-trees/images/B-trees-insert3.gif)

- **Definition:** An organizational structure for information storage in the form of a tree where all the terminal nodes are the
same distance from the base and all nonterminal nodes have n - 2n subtrees

- Often used in database systems or other applications where data is stored externally on disks and keeping tree shallow is important

##Disk Based Data Structures

- So far searchtrees were limited to main memory structures

- Counter-example: transaction data of a bank > 1GB per day

- Consequence: make a search tree structure secondary-storage-enabled

##Binary Trees vs. B-trees

- Size of B-tree is determined by the page size. One page - one node.

##B-Tree Definitions

- Every leaf has the same depth which is the tree's height h

- In a B-tree of a **degree** t:

- Every node other than the root must have at least t-1 keys. Every internal node other than the root thus has at least t children

- Every node may contain at most 2t-1 keys. Therefore, an internal node may have at most 2t children.

- The root node has between 0 and 2t children (ie. between 0 and 2t-1 keys)

```
degree-t

Every node (except Root):
  Minimum # of Keys: t-1 :  2 - 1 = 1
  Maximum # of keys: 2t-1 : 2x2 - 1 =3

Root:   Children

0   ->  0

2t-1 -> 2t
```

##Height of a B-tree

- B-tree T if height h, containing n >= 1 keys and minimm degree t >= 2, the follwing restriction on the height holds: h <= log_t (n+1)/2

Example: Google Search is built on variation of B-tree. It is very important b/c majority of search engine use it.

- How are keys stored? The best way to implementing keys is a bi-directional linked list. 

```
n: total # of keys

n >= (|x|) + (2(t-1))+(2t(t-1))+(2t^2 * (t-1)) + ...

n >= 1 + (t-1)(2 + 2t + 2t^2 + ...) ->2 [n E (i = 1)] t^n = 2 x (t^n -1 / t-1)

n >= 1 + (t-1)* 2 * (t^n -1 / t-1)

n >= 1 + 2t^n - 2

2t^n <= n+1 -> t^n <= (n+1)/2 -> h <= log_t (n+1)/2
```
