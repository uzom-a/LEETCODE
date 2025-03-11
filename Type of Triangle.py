class Solution:
    def triangleType(self, nums: List[int]) -> str:
        """
        U-Understand
        identify what type of triangle it is according to the items in the nums array

        M-Match
        array, two pointers

        P-Plan
        check if 2 items are the same;
        if yes check if three items are the same if no return isosceles but if yes return equilateral
        if none return scalene

        I-Implement
        code implementation below
        """

        i = 0
        
        if (nums[i] + nums[i+1]) > nums[i+2] and (nums[i+1] + nums[i+2]) > nums[i] and (nums[i+2] + nums[i] > nums[i+1]): #you have to make sure the sum of any two sides is greater than the last slide
            if nums.count(nums[i]) == 3: #catcth them from the first number
                return "equilateral"

        
            seen = set(nums)
            if len(seen) == (len(nums) - 1):
                return "isosceles"

            if len(seen) == len(nums):
                return "scalene"
        else:
            return "none"
            
        #Time Complexity : O(n) because you have to iterate through each item in nums in order to change it into a set
        #Space Complexity: O(n) remember Uzoma, you used an extra set
