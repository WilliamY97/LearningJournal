"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

SOLUTION: Iterate through the list of words and record index if word is word1 or word2. Check if you have an index
for word1 and word2 recorded, if so check if the difference is less than the current minDistance. If so record it.
"""

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        index1 = index2 = -1
        minDistance = len(words)
        
        for i in range(0,len(words)):
            
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
            
            if index1 != -1 and index2 != -1:
                minDistance = min(minDistance, abs(index1-index2))
        return minDistance
