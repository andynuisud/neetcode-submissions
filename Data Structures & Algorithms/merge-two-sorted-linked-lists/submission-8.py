# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
            Add them to a new linked list alternating. 
            If there is anything else just append it to the end of the linked list. 
        """

        l1Head = list1
        l2Head = list2

        current = ListNode()
        dummy = current

        while l1Head and l2Head: 
            #While both of these conditions are fulfilled

            if l1Head.val >= l2Head.val:
                dummy.next = ListNode(l2Head.val)
                dummy = dummy.next
                l2Head = l2Head.next
            else:
                dummy.next = ListNode(l1Head.val)
                dummy = dummy.next
                l1Head = l1Head.next

        while l1Head: 
            dummy.next = ListNode(l1Head.val)
            dummy = dummy.next

            l1Head = l1Head.next

        while l2Head: 
            dummy.next = ListNode(l2Head.val)
            dummy = dummy.next

            l2Head = l2Head.next

        return current.next
            