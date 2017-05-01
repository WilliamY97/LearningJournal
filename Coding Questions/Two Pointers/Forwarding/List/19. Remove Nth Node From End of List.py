class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        dummy.next = head
        
        for i in range(n):
            head = head.next
        
        while head:
            cur = cur.next
            head = head.next
        
        cur.next = cur.next.next
        return dummy.next
