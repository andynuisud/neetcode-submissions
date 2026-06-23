# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
        dummy = ListNode(0)
        current = dummy
        carry = 0 

        while l1 or l2 or carry: 
            val1 = 0 
            val2 = 0 
    
            if l1: 
                val1 = l1.val 
            if l2: 
                val2 = l2.val 

            total = val1 + val2 + carry 

            if (total) >= 10: 
                carry = 1
            else:
                carry = 0 

            total = total % 10 

            current.next = ListNode(total)
            current = current.next

            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

        return dummy.next
