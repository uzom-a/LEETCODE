class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] #it will definitely have the first element
        n = len(nums)
        for i in range(1, n):  #so start from the second elemnt since the new prefix array has the first element
            prefix.append(nums[i] + prefix[-1])
            
        return prefix
            
