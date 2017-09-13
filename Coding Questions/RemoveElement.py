"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


def removeElement(self, nums, val):
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j
