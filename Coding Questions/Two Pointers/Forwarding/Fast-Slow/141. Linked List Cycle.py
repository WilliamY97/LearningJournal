class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or slow == None: return False
            if fast.next:
                fast = fast.next
                slow = slow.next
            fast = fast.next
        return True
