class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = float('inf')
        sum = 0
        head = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res, i - head + 1)
                sum -= nums[head]
                head += 1

        if res <= len(nums):
            return res
        else:
            return 0
