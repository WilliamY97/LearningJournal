# Hash Tables

A hash table is a data structure that can map **keys** to **values**. A **hash function** is used to compute an index into an array of
*buckets*, from where the value can be found.

## Hash Functions

A hash is a *restatement of something that is already known*. The ultimate goal will be to *hash* any object to a value. Any function
that performs this is called a hash function.

### Properties of Hash Functions

1a. It must be fast - ideally O(1)
1b. It must be deterministic: it must always return the same value for the same object
1c. If two objects x and y are considered equal, their hash values must be equal, i.e. h(x) = h(y)
1d. If two objects are chosen at random, there should be a very low probability that they have the same hash value
1e. The distribution of hash values in 0 to 2^32-1 should be approximately even (that is the distribution of values
is either uniform distribution or a Poisson distribution)

## Predetermined Hash Values

