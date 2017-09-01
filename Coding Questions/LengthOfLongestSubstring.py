# Given a string, find the length of the longest substring without repeating characters.

#O(n^3) solution often times out. The method is to iterate through with two loops and check for
# every single substring in the string. Then for every substring you add their letters into a set
# only before checking if it contains it. If it does then the string is invalid but if it doesn't
# the new maxValue is the substring length. The space complexity is O(min(n,m)) where n is the
# length of the string that upperbounds it and m is the number of distinct characters in the string

#O(n) solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = maxValue = 0
        h = {}

        for i in range(len(s)):
            if s[i] in h and start <= h[s[i]]:
                start = h[s[i]]+1
            else:
                maxValue = max(maxValue, i-start+1)
            h[s[i]] = i
        return maxValue

