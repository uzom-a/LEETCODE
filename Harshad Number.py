class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        """
        U-Understand
        add the two digits 
        check if the sum is a perfect divisor of the integer given


        M-Match
        math

        P-Plan
        change the integer to a str
        add the first element and last element of the str
        divide the integer by the sum
        if divisible
            return the sum
        else
            return -1

        I-Implement
        look at the code below
        """
        if x < 10:
            return x

        nums = str(x)
        sum_of_num = int(nums[0]) + int(nums[1])

        return sum_of_num if x % sum_of_num == 0 else -1

        """
        R-Review
        made so many tiny errors

        E-Evaluate
        Time Complexity: O(n)
        Space Complexity : O(n)
        """




