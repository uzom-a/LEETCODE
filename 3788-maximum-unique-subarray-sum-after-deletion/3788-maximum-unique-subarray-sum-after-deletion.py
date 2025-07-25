class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxx = max(nums)
        i = 0
        if maxx < 0: #if the largest number is negative then that is the best sum you can get so return it
            return maxx
        else:
            nums = list(set(nums)) #removing duplicates to make the array unique
            nums = [num if num > 0 else 0 for num in nums] #keeping only positive numbers
        # print(nums)
        return sum(nums)

        #TIME COMPLEXITY : O(n)
        # Space Complexity:O(n)