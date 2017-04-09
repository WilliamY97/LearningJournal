# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

"""
SOLUTION: The additional logic required in this second part of the question is to find the max depth through a helper function
and then perform the same sum calculation as before but this time, when we recurisvely traverse into nested lists we decrease
the depth value since it's greatest to lowest depth
"""

class Solution(object):
    def depthSumInverse(self, nestedList):
        maxDepth = self.findDepth(nestedList)
        return self.depthSum(nestedList,maxDepth)
    
    def findDepth(self, nestedList):
        if not nestedList: return 0
        maxDepth = 1
        for val in nestedList:
            if val.getList():
                maxDepth = max(self.findDepth(val.getList())+1,maxDepth)
        return maxDepth
    
    def depthSum(self, nestedList, depth):
        if not nestedList: return 0
        sum = 0
        for val in nestedList:
            if val.isInteger():
                sum += val.getInteger() * depth
            elif val.getList():
                sum += self.depthSum(val.getList(), depth-1)
        return sum
                
