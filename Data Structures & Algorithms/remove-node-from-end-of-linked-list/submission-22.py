# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
            We just move the right pointer to n
            Keep the distance of n between these two
        """

        dummy = ListNode(0, head)
        current = dummy 

        left = current
        right = current

        index = 0

        while index < n: 
            right = right.next
            index += 1

        #now we iterate through the rest

        while right and right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next