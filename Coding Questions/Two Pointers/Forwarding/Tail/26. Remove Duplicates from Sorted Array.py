"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

def removeDuplicates(self, nums):
    if not nums: return 0
    tail = 0

    for i in range(1,len(nums)):
        if nums[i] != nums[tail]:
            tail += 1
            nums[tail] = nums[i]
    return tail + 1

"""
SOLUTION:

Have two pointers, one fast (start one ahead), one slow. Have the fast pointer compare itself with the slow pointers value.
If they're the same then it's a duplicate and we can ignore it and keep moving the fast pointer. If the fast compared to
the slow is different then the slow pointer can move over one index and set that index to the value from fast. This will
ensure that everytime a unique value is detected we can simply have the slow pointer repopulate the index from the start
with these new values. At the end return the pointer index + 1 (because it started at 0) and the array should be formatted
to have all the unique values in sequence from the start - with whatever buffer leftover at the end indices - but that
doesn't matter just as the question states.

"""
