class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            num = nums[i]
            complement= target - nums[i]
            if complement in d:
                return d[complement] , i
            d[num] = i

"""
Time complexity - O(n)
Space Complexity - O(n)
"""
