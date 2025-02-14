class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float('-inf')
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0

        return max


        #This is Kadane's algorithm
        """
        If current_sum is positive, it continues to add the next element because it could lead to a larger sum.
If current_sum is negative, it resets to 0 because starting fresh is better than carrying forward a negative sum
        """
        #Time Complexity = O(n)
        #Space Complexity = O(1)
