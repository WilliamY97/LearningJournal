# Sorting Algorithms

## Quicksort

A strategy to sort a list by dividing it into sub-lists: select one entry in the list as a *pivot* and seperate all other entries as to
whether they aere smaller than or larger than this pivot.

Using this idea, quicksort is, on average, faster than merge sort and has the following properties.

||  Run Time     | Memory
---- | ----- | ----
Average Case   |     O(nlog(n))          | O(log(n))
Worst Case   |     O(n^2)          | O(n)
