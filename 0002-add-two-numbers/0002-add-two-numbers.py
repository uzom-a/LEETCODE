# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Understand
            -we need to add the digits in the two linked list but in reverse order

            Input: two linked list
            Output: one Linked list
            Constraints: 4 + 6 = 10 
            Edge Cases : carry_over variable

        Plan
            init ll
            init carry_over
            init curr1 to head of ll1
            init curr2 to head of ll2

            iterate through both linked list ;nothing is out of bound
                sum = curr1.val + curr2.val
                carry_over = sum // 10
                digit = sum % 10

            return ll


        """

        temp = ListNode(0)
        move = temp

        curr1 = l1
        curr2 = l2
        rem = 0

        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            sum = val1 + val2 + rem
            rem = sum // 10
            digit = sum % 10
            move.next = ListNode(digit)

            #move the variales
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            move = move.next

        if rem:
            move.next = ListNode(rem) #to account for multiple carry overs
        return temp.next

    #Time Complexity = O max(n,m)
    #Space Complexity = O max(n,m)

