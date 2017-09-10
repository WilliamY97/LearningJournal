class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxVal = 0
        d = collections.defaultdict(int)
        
        for i in range(len(s)):
            d[s[i]] += 1
            while len(d) > 2:
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    del d[s[start]]
                start += 1
            maxVal = max(maxVal, i-start+1)
        return maxVal
