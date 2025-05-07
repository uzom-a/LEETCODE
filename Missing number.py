class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        check  = set()
        
        for i in range(n+1):
            check.add(i)
        
        for number in check:
            if number not in nums:
                return number
            
        #time complexity = O(n^2)
        #space complexity = O(n)
"""
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

#Time complexity is O(n)
#space complexity is O(n)
""""""
