from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        #FIRST FUND OUT THE UNIQUE NUMBERS
        unique_nums = set(nums)
        this is a bit repititive because we can just use the hash map to 
        """
        ans = 0
        
        count_nums = Counter(nums) #basically create the dictionary which would only have unique keys
        
        for key, value in count_nums.items():
            if value > 2:
                continue
            elif value == 1:
                ans = max(ans, key)
                
        return ans if ans else -1
