# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #remember you have to go through the head to solve the linked list
        curr = head 
        prev = None

        while curr:
            t = curr.next #we don't want to loose the ll
            curr.next = prev #make the head set to nothing
            prev = curr #move prev
            curr = t #move curr

        return prev #at the end prev would turn tp the head

        """Time Complexity : O(n)
        Space Complexity: O(1)"""
