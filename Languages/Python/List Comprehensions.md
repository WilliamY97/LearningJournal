# List Comprehensions

Python supports list comprehensions which is used to create lists in a very natural way.

Lists can contain any type of elements, including strings, nested lists and functions. You can even mix different types within a list.


```
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print primes
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```
The result that you want added to the list is placed at the start of the list, the rest of it is the logic that goes through producing
the values.

Like the example above, you can develop a list with nested for loops. The nesting is read from left to right.
