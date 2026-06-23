# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
            Iterate from start to n, then the slow node would be right before nth node
            After this just reroute the node

            slow = slow.next.next
        """
        dummy = ListNode(0, head)
        current = dummy
        slow = current
        fast = current

        index = 0 

        while (index < n):
            fast = fast.next
            index += 1
        

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next



