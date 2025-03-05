class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        ans= []
        a = 2

        while a:
            for i in range(len(nums)):
                ans.append(nums[i])

            a -= 1

        return ans

        """
        time complexity : O(n)
        space complexity: O(n)
        """

        
