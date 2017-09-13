"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

SOLUTION: This is to find the sequential subarray that has the greatest sum. Using Kadane's algorithm we iterate through the
values in the array and check if they plus the currentTotal is greater than the value itself. If the value itself is greater
than we keep that value because the value itself is a greater total than the sequence before it. We compare this currentTotal
with the totalMax which is our record of the greatest sum so far throughout the array.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentMax = totalMax = nums[0]
        
        for i in range(1,len(nums)):
            # the thought process is - if nums[i] is larger than the held max + itself then the values before nums[i] are smaller than
            # nums[i] and we can start over at nums[i] as the start of the subarray now instead
            currentMax = max(nums[i],currentMax + nums[i])
            totalMax = max(totalMax,currentMax)
        
        return totalMax
