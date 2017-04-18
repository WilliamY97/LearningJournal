class Solution(object):
    def trap(self, height):
        if height is None or len(height) == 0:
            return 0
        
        water = 0
        l, r = 0, len(height)-1
        
        while l<r and height[l+1] >= height[l]:
            l += 1
            
        while l<r and height[r-1] >= height[r]:
            r -= 1
        
        while l<r:
            left = height[l]
            right = height[r]
            
            if left < right:
                while l<r and height[l] <= left:
                    water += left - height[l]
                    l += 1
            else:
                while l<r and height[r] <= right:
                    water += right - height[r]
                    r -= 1
        return water
                
