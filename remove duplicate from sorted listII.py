# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, head)
        first = temp
        second = head

        while second and second.next:
            found = False
            while second.val == second.next.val:
                second = second.next
                found = True
            if found:
                first.next = second.next
            else:
                first = first.next
            second = second.next
        return temp.next
