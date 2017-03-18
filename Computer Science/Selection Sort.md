# Selection Sort

- Basic idea behind selection sort is to divide list into sorted and unsorted portions.

- At each step, a number is moved from unsorted to sorted.

- Even though a number might be in the right location, our algorithm has no way
of knowing that until the entire list is sorted

- We consider entire list as unsorted until we sort it ourselves

**Goal:** We want the list to be in ascending order. We'll want to build up our
list from left to right, smallest to largest.

- To do that we'll need to find the minimum unsorted element and put at the end
of the sorted portion. 

- Since list is not sorted, the only way to do that is to look at each element
in unsorted portion and remember what element is lowest - then compare every element
to that.

- Look at first element and remember that as minimum
- Iterate through list and compare each number with the minimum - if it's lower then
the minimum = that number.
- Swap whatever number is first with the one that is minimum. 
- We know that value swapped is both the smallest element and the element at the beginning
- We start at the next element and repeat. 
