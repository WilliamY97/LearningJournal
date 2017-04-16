class Solution(object):
    def twoSum(self, numbers, target):
        if numbers is None or len(numbers) == 0:
            return []
        
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum > target:
                r -= 1
            else:
                l += 1
        return []
                
        
