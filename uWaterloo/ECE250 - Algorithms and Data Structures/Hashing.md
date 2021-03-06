# Hashing

A dictionary is a data structure that stores key-value pairs and supports the operations (Insert, Search, and Delete). We can implement
dictionaries in a bunch of ways: balanced binary search tree, which supports these actions in O(logn) time. We can also use a doubly
linked list which supports Insert/Delete in O(1) time but Search in O(n) time. But using a hash table, we can do all of this in O(1)
time.

## Hash Tables

A hash table is a data structure that can map **keys** to **values**. A **hash function** is used to compute an index into an array of
*buckets*, from where the value can be found.


Algorithm |  Average     | Worst Case
---- | ----- | ----
Space   |     O(n)          | O(n)
Search   |     O(1)          | O(n)
Insert   |     O(1)          | O(n)
Delete   |     O(1)          | O(n)

## Hash Functions

A hash is a *restatement of something that is already known*. The ultimate goal will be to *hash* any object to a value. Any function
that performs this is called a hash function.

### Properties of Hash Functions

1. It must be fast - ideally O(1)
2. It must be deterministic: it must always return the same value for the same object
3. If two objects x and y are considered equal, their hash values must be equal, i.e. h(x) = h(y)
4. If two objects are chosen at random, there should be a very low probability that they have the same hash value
5. The distribution of hash values in 0 to 2^32-1 should be approximately even (that is the distribution of values
is either uniform distribution or a Poisson distribution)


