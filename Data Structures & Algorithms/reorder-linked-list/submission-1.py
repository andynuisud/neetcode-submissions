# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        """
            1. Finding the middle using fast and slow pointers
            2. Reverse the second portion
            3. Concatenate them as they alternate
        """

        slow = head 
        fast = head.next 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        #Slow would be our middle of the linked list 

        previous = None
        current = slow.next 
        slow.next = None

        while current: 
            temp = current.next
            current.next = previous 
            previous = current
            current = temp

        first, second = head, previous 

        while second: 
            temp1, temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1 

            first, second = temp1, temp2