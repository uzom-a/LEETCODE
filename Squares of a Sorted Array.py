class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        nums.sort()

        return nums

        """
        Time complexity - O(nlogn)
        Space Complexity - O(1)
        """
