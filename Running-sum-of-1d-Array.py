class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        U-Understand
        add the numbers one step at a time

        M-Match
        array

        P-Plan
        create a new array called result
        iterate through the array
        append the sum to the result array

        I-Implement
        look at the code below
        """

        result = []
        sum = 0

        for i in range(len(nums)):
            sum = sum + nums[i]
            result.append(sum)

        return result

        """
        R-Review
        the fact it worked in one try is giving genius

        E-Evaluate
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
