# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next: #base case
            return head.val + head.next.val

        #FIND THE MIDDLE OF THE LINKED LIST AND THE LENGTH
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #the slow pointer is at the middle now

        #REVERSING THE SECOND HALF OF THE LINKED LIST
        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        #STEP 3 WITH NEW POINTERS
        first_pair = head
        second_pair = prev #prev is the new head of the half reversed linked list
        

        #GETTING THE SUM
        ans = 0
        while second_pair:
            ans = max(ans, first_pair.val + second_pair.val)
            first_pair = first_pair.next
            second_pair = second_pair.next

        return ans
            
