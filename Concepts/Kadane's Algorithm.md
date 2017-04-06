# Kadan's Algorithm

A solution to the **maximum subarray problem**. This is the task of find the adjoining subarray in a 1-D array of numbers which has
the largest sum.

Example

```
-2, 1, -3, 4, -1, 2, 1, -5, 4```the subarray with the largest sum is [4 -1 2 1] = 6
```
## Brute Force Approach

Take all possible sub-arrays and check which one has the maximum sum amongst them.

```
For each sub-array
  calculate current_sum
  if (current_sum > total_sum)
    total_sum = cur_sum
```
Time Complexity: O(n^3)

## Process of Algorithm

1. Initialize current_max = array[0] and total_max = array[0]

2. For i=1 to n-1 (0-indexing)
     {
     current_max = max(a[i],array[i]+current_max)
     total_max = max(current_max, total_max)
     }

3. Print total_max as your final result

Time Complexity: O(n)
