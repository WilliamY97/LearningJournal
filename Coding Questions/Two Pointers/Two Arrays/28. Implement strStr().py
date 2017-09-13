class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        
        for i in range(m+1):
            for j in range(n+1):
                if j == n:
                    return i
                # This stop is the case when i is m-1 or m and the j is on the first letter of needle
                if i+j == m:
                    return -1
                if haystack[i+j] != needle[j]:
                    break
