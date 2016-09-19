# Hash Tables

A data stucture that maps keys to values for a highly efficient lookup.

## Implementation CTCI

![alt tag](hashtable.png)

It can be implemented using an array of linked lists and a hash code function. In order to insert a key (could be a string or any other data type) and value, we do the following:

1. Compute the key's hash code, which will usually be an *int* or *long*. NOTE: Two different keys can have the same has code, as there may be an infinite number of keys and a finite number of ints.
2. Map the hash code to an index in the array. This can be done with something like hash(key) % array_length. Two different hash codes can map to the same index.
3. At this index, there is a linked list of keys and values. Store the key and value in this index. We must use a linked list because of collisions. You could have two different keys with the same hash code, or two different hash codes that map to the same index.

*Retrieval:* In order to retrieve a value pair by its key, you repeat this process. Compute the hash code from the key, and then compute the index from the hash code. After, search through the linked list for the value with this key.

*Worst Case:* # of collisions is high O(N), where N is the number of keys.
*Best Case:* # of colliisions is low - lookup time is O(1).
