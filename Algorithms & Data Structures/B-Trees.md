#B-Trees

- **Definition:** An organizational structure for information storage in the form of a tree where all the terminal nodes are the
same distance from the base and all nonterminal nodes have n - 2n subtrees

##Disk Based Data Structures

- So far searchtrees were limited to main memory structures

- Counter-example: transaction data of a bank > 1GB per day

- Consequence: make a search tree structure secondary-storage-enabled

##Binary Trees vs. B-trees

- Size of B-tree is determined by the page size. One page - one node.

```
degree-t

Every node (except Root):
  Minimum # of Keys: t-1
  Maximum # of keys: 2t-1

```
