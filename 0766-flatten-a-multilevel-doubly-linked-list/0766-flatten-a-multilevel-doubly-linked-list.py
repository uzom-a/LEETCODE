"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            if curr.child:
                new_normal = curr.next #saving the next node
                tail = curr.child #pointer to move around the child list
                # move to the tail of the child list
                while tail.next:
                    tail = tail.next

                # attach the saved next node after the tail
                tail.next = new_normal
                if new_normal: 
                    new_normal.prev = tail

                # attach child list after current node
                curr.next = curr.child
                curr.child.prev = curr

                #remove child pointer
                curr.child = None

            curr = curr.next

        return head
