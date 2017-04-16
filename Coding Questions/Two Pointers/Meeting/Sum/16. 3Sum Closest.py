class Solution(object):
    def threeSumClosest(self, nums, target):
        if nums == None or len(nums) == 0:
            return 0
        
        nums.sort()
        res = 2147383647
        
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(target-temp) < abs(target-res):
                    res = temp
                
                if temp == target:
                    return temp
                elif temp > target:
                    r -= 1
                else:
                    l += 1
        return res
