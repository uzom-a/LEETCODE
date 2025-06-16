# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp_head = ListNode('X', next = head)
        before = temp_head
        curr = head
        l = 1

        while l < left:
            before = before.next
            curr = curr.next
            l += 1

        last = None
        left_node = curr

        while left <= right:
            saved = curr.next
            curr.next = last
            last = curr
            curr = saved
            left += 1


        before.next = last
        left_node.next = curr

        return temp_head.next
