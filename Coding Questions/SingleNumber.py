"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

SOLUTION:

XOR the elements. Using commutative property of XOR the elements that appear twice are A^A = 0. The final element
that is alone will evaluate to B ^ 0 = B
"""

class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        for val in nums:
            ans ^= val
        return ans
