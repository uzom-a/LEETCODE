class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        U-Understand
        find the maximum products of two elements that are 1times less

        M-Match
        array

        P-Plan
        create a max
        iterate through i and j
        replace max if the two products produce the maximum number

        I-Implement
        look at the code below

        """
        maximum = float('-inf')

        for j in range(len(nums)):
            for i in range(len(nums)):
                if i != j: #in the description of the question
                    multiply = (nums[i] - 1) * (nums[j] - 1)

                    if multiply > maximum:
                        maximum = multiply

        return maximum

        """
        R-Review

        E-Evaluate
        Time Complexity - O(n^2)
        Space Complexity - O(1)
        """
