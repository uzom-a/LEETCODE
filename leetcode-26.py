class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0   #holding the place of the last unique element
        second = 1  #checking to find the next unique element
        n = len(nums)

        while second < n:
            if nums[first] == nums[second]:
                second += 1

            if second >= n: #I did this because of this testcase [1,1]
                break

            if nums[first] != nums[second]:
                first += 1
                nums[first] = nums[second]
                second += 1

        return first + 1  #I had to add one because of the 0-index


    """Time Complexity: O(n)
    Space Complexity : O(1)"""
