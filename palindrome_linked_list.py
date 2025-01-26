# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_version = []

        itr = head
        while itr:
            list_version.append(itr.val)
            itr = itr.next

        left = 0 
        right = len(list_version) - 1

        while left < right:
            if list_version[left] == list_version[right] and right > -1:
                left += 1
                right -= 1
            else:
                return False
        return True
