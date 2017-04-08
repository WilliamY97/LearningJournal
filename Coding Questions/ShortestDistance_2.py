"""
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

SOLUTION: The key to this problem is that there is now a variety of potential 2 words to find the distance of. This class can
optimize this by storing the position of the word values from the words list into a hashtable and then in the method "shortest"
we can immedietly know the indices for word1 and word2 and check the distance between them in a while loop. This while loop will
check the list of indices for word1 and word2 and find the difference between them. Each time updating the result with the smallest
distance with the min(res, abs(d[word1] - d[word2]))
"""


class WordDistance(object):

    def __init__(self, words):
        self.d = {}
        for i, w in enumerate(words):
            self.d[w] = self.d.get(w,[]) + [i]

    def shortest(self, word1, word2):
        a,b = self.d[word1], self.d[word2]
        m,n,i,j,res = len(a),len(b),0,0,sys.maxsize
        
        while i < m and j < n:
            res = min(res,abs(a[i]-b[j]))
            
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res
