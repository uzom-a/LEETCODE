import math
class Solution:    
    def get_count(self, n :int) -> int:
   		return math.floor(math.log10(n)) + 1

    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            digits = self.get_count(num)
            if digits % 2 == 0:
                count += 1

        return count

    #time complexity : O(n)
    #space complexity : O(1)

    
