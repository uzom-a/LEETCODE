class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        PSEUDOCODE
        init first = 0
        init second = 1

        while first < len(nums) and second < len(nums):
            if num at first == num at second:
                while second < len(nums) and num at first == num at second:
                    move second forward
            else:
                swap num at first + 1 and num at second
                move second
                move first

        return first

        """

        first = 0
        second = 1

        while first < len(nums) and second < len(nums):
            if nums[first] == nums[second]:
                while second < len(nums) and nums[first] == nums[second]:
                    second += 1
            else:
                nums[first + 1], nums[second] = nums[second], nums[first + 1]
                second += 1
                first += 1

        return first + 1 
        #note if you return first then that would be an off by 1 error because first gives you the index not the length of unique elements

"""
        Time Complexity: O(n)
        Space Complexity: O(1)#it has to be done inplace eitherways soo
"""