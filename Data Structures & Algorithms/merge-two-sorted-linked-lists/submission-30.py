# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
     
        """
           Return a new head or Keep in order 
        """

        #We want the tail to include the rest of the linked list after adding it 

        dummy = ListNode(0)
        current = dummy
        tail = dummy

        while list1 and list2: 
            if list1.val < list2.val: 
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1: 
            tail.next = list1

        if list2: 
            tail.next = list2 

        return current.next

