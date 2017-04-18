# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if head == None or head.next == None: return head
        k %= self.getLen(head)
        
        current = dummy = ListNode(0)
        dummy.next = head
        
        for i in range(k):
            head = head.next
            
        while head.next:
            head = head.next
            current = current.next
        
        current = current.next
        
        head.next = dummy.next
        dummy.next = current.next
        current.next = None
        
        return dummy.next
        
        
    def getLen(self,head):
        len = 0
        while head:
            len += 1
            head = head.next
        return len
