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

- Often helpful in questions pertaining to word validation. (Ex. **Check if this is you know..., walk through this table and find all
the..., walk through this board and find all the words, or given list of strings, find all celebrity names.

- When you see something that has some word list validation think about whether or not a trie may be useful.

Ex. Somebody is typing a word and when it is not found, underline it - a Trie would be good for this.

## Keeping State

- We can store where we are in the tree. So when the user types the very next character, an A, we just look immediately is A a child
rather of last look up than starting from scratch.

Two Ways To Implement This:

1. Keeping state within trie
2. Return node reference
