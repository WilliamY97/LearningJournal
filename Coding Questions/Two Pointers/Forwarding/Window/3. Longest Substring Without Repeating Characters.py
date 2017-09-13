class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tail = 0
        maxVal = 0
        d = {}
        
        for i in range(len(s)):
            if s[i] in d and tail <= d[s[i]]:
                tail = d[s[i]]+1
            else:
                maxVal = max(maxVal,i-tail+1)
            d[s[i]] = i
        return maxVal
