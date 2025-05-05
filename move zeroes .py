class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #let's try two pointers shall we

        #INTIALIZE VARIABLES
        n = len(nums)
        f = 0
        s = 1

        for s in range(n):
            if nums[s] == 0:
                s += 1
            else:
                nums[f], nums[s] = nums[s], nums[f]
                f += 1
                s += 1
    
        return nums
