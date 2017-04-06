"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Solution: Iterate through list and check if an element can be the minValue (aka it's lower) or else subtract that element from the
current minValue and see if that is greater than the current MaxValue. If so replace it because that's a better sale.

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minValue = 999999
        maxValue = 0
        for val in prices:
            if val < minValue:
                minValue = val
            else:
                if val - minValue > maxValue:
                    maxValue = val - minValue
        return maxValue
