"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

SOLUTION: Set up a hashtable and the add method will add the numbers to this table by their occurences. After in the find method
check the table if the conjugate of the value exists in the table. If it does then there exists two values that sum up the the
value. The edge case is when the two values are the same. In this case we must double check that they are indeed equal with
(value - v != v). If it is true then we need to check that d[v] > 1 so that we have two of those values in the DS to sum to the value. 

"""


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.d:
            self.d[number] += 1
        else:
            self.d[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        d = self.d
        for v in d:
            if value - v in d and (value - v != v or d[v] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
