# Two Pointers

Two pointer questions can be seperated into three categories with subcategories:

### 1. Meeting (Sum or Array)
### 2. Forwarding (List, Tail, Window, or Fast&Slow)
### 3. Two Arrays

## Meeting

### Sum Subcategory

**167. Two Sum II - Input Array is Sorted**

Use two pointers left and right of the array and increment/decrement them if the sum of the values between them is greater or smaller than
the expected target. If the sum is the target then return it. Left pointer should be always smaller than right pointer. If they cross then
the algo is finished and return [] because no values add up to target.

**15. 3Sum**

We sort the array and then iterate through it where at each value we set up a left and right pointer on the values ahead of it and then this question breaks down to 2Sum. The only difference being that we return the set of values for the solution and when we hit the target
we need to move the left and right pointer once to check if any more values with the current pivot can get to the target. The edge case here is to be careful of reoccuring values that are the same. If the current pointer value is equal to the next value then just move the
pointer. Two while loops, one for each pointer can accomplish this. This ensures we don't get the same solution set over and over again.

**16. 3Sum Closest**

**16. 3Sum Smaller**

**16. Triangle Count**

**16. 4Sum**


