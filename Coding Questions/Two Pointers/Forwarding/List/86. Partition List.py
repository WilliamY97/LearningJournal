# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None: return None
        h1 = curr1 = ListNode(0)
        h2 = curr2 = ListNode(0)
        
        while head:
            temp = head.next
            if head.val >= x:
                curr2.next = head
                curr2 = curr2.next
                head.next = None
            else:
                curr1.next = head
                curr1 = curr1.next
                head.next = None
            head = temp
        
        curr1.next = h2.next
        
        return h1.next
