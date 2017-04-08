"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Solution: The issue with having the words be the same is that we need to be able to assign it to word1 and then word2 to check the
distance between them. To know which one to assign the word indice to, we use a flag that alternates so that word1 can hold it and
then word2, repeat. 
"""

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        res, flip, = len(words), True
        index1,index2 = -1,-1
        for i,w in enumerate(words):
            if w == word1 and flip:
                index1 = i
                if word1 == word2: flip = False
            elif w == word2:
                index2 = i
                if word1 == word2: flip = True
                
            if index1 != -1 and index2 != -1:
                res = min(res,abs(index1-index2))
        return res
        
