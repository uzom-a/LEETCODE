class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        def reverse(listt, left, right):
            
            while left < right:
                # swap
                listt[left], listt[right] = listt[right], listt[left]
                left += 1
                right -= 1
            
            

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k % n - 1)
        reverse(nums, k % n, len(nums) - 1)