# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        slow = head
        fast = slow.next
        
        while fast:
            if slow.val == fast.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
                
        slow.next = None #to remove any trailing duplicates
        return head
                
        #Time Complexity is O(n)
        #Space Complexity is O(1) because you know how little space the pointers take in python
