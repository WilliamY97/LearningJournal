"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

SOLUTION: Go through list and check if the element is a integer -> if so then just add it to the sum.
If it's a list then call the method on it with a deeper depth. This will go through the nest and find
the sum recursively.
"""
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """



class Solution(object):
    def depthSum(self, nestedList,depth=1):
        sum = 0
        for val in nestedList:
            if val.isInteger():
                sum += val.getInteger() * depth
            elif val.getList():
                sum += self.depthSum(val.getList(),depth + 1)
        return sum
