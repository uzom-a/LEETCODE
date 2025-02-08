# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2
        new_ll = ListNode("None")
        curr_new = new_ll

        while curr1 or curr2:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            curr_sum = v1 + v2 + carry

            curr_new.next  = ListNode(curr_sum % 10)
            carry = curr_sum//10

            curr_new = curr_new.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        curr_new.next = ListNode(carry) if carry else None
        
        return new_ll.next
