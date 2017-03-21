# Tries

A Trie is a data structure which is a type of tree that is often used to store characters. Each node stores a character and when
we look at the path from the root down to that node, that node is really representing a word or a part of a word.

## Advantage

- Allows for quick lookups of words with certain prefixes

## Implementation

- We implement a class node, but instead of a left/right node like in a binary search tree, we have some sort of either array
of the children, or a lookup table that maps from a character to that node. This allows us to immediately say do you have a
child that is an "A". And is that child a complete word or just a prefix. So each node also has some sort of flag in it
(Ex. **boolean isCompleteWord**) that represents a complete word. 

## When Is It Used?
