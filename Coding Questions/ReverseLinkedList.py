# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
SOLUTION: The goal of this problem is to change the pointer of every node (.next) to point to its previous node. This requires a
change in references. First we save current.next to a temp variablem, then point current.next to the previous node. The prev variable
will then point to the current variable and current will equal the temp.
"""

class Solution(object):
    def reverseList(self, head):
        if head is None: return None
        prev = None
        current = head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
