# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        PSEUDOCODE
        I don't need nodes that the values are equal 
        I need to detect nodes that point to the same memory that is essentially the same object
        """
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next

        while headB:
            if headB in seen:
                return headB
            headB = headB.next

        return None

        """
        Time Complexity is O(n+m) because we are iterating through both lists
        Space Complexity is O(n)
        """
