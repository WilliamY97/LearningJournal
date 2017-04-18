# Two Pointers

Two pointer questions can be seperated into three categories with subcategories:

### 1. Meeting (Sum or Array)
Having two pointers approach each other from left and right side
### 2. Forwarding (List, Tail, Window, or Fast&Slow)
### 3. Two Arrays

## Meeting

Template Code:

```
Given some array A:
if height is None or len(height) == 0:
    return 0
r,l = 0, len(A)-1
while l<r:
  some logic
  r += 1
  l -= 1
return something

```

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

We're trying to find the closest value to the target here. It's the same as three sum, but now we're not looking for all sets of solutions so we don't need to avoid re-occuring values with while loops. Simply we find the sum and compare it with the current result value and see which one is closer to the target. If the sum is the target then return it - otherwise move left or right pointer

**16. 3Sum Smaller**

**16. Triangle Count**

**16. 4Sum**

### Array Subcategory

**11. Container with Most Water**

This is a two pointer based question - the strategy is that knowing when we have two heights - we will only be able to hold water based
on the height of the lower one. This being known we should always move the pointer that has the smaller height as it may point to a greater height.

**42. Trapping Rain Water**

Core logic is that when one wall is greater then the other we know that anything coming after the lower wall that is more lower will
have water that can be retained (because whatever comes after we know there will be a wall tall enough to hold it). We only stop a
pointer when it is at a height greater than the original. Then we re-check which wall is higher again and iterate the lower pointer to
see how much water we can collect before reaching a higher wall again. When the two pointers meet we have collected all water from both
sides. NOTE: Remember to keep track of when we re-valuate which wall is higher and when we're moving the walls to collect water that l is smaller than r pointer index.

**125. Valid Palindrome**

Strategy is to have two pointers. Any thing that isn't alphanumeric we skip. Check if they're equal - if not it's not palindrome. Then
move both pointers. If left < right at the end, then we know it's a palindrome

## Forwarding

### List Subcategory

**1. Partition List**

Set up 4 pointers, 2 for each node list. If value is greater or less than x - add it to the appropriate list. At the end link the
two lists by taking the smaller value of x list and attach it's final pointer to the head of the other list.

**2. Rotate List**

One pointer to be dummy on head. Find length of list using helper function. Modulus the k value by length. Move the head by k amount
after. Then move k to end of list and move current pointer from dummy. Then move current pointer one more time (could this be changed
to just start from head?). Then head points to dummy.next. Dummy.next points to current.next. Current.next points to none. List is
rotated.

**3. Palindrome Linked List**

**4. Remove Nth Node From End of List**


### Tail Subcategory

### Window Subcategory

### Fast&Slow Subcategory


