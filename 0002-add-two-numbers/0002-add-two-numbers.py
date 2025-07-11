# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur = dummy #cur is the pointer for this linkedlist
        carry = 0

        while l1 or l2 or carry: #if carry still has a digit we should continue the while loop to satisfy that edge case even if carry has no digit
            v1 = l1.val if l1 else 0 #get the value from the first linkedlist
            v2 = l2.val if l2 else 0 #get thevalue from the second LinkedList

            val = v1 + v2 + carry #normal elementery school addition
            carry = val // 10 #to get the tens place for the carry
            val = val % 10 #to keep the val at the units place

            cur.next = ListNode(val) #create a new node for this value we have added together

            #incrememnt pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        """
        Understand
        the ll is stored in reverse order which makes it easier to add 

        Match
        linked list

        Plan
        create a dummy node
        create a pointer 
        iterate through the linked list
        add the values carry over the value if the addition is multiple digits
        add those values to the new linked list
        
        Implement
        look at the code above

        Review

        Evaluate
        time complexity-O(n + m)
        space complexity - O(n + m)

        """