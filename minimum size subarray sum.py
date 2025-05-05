class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #INTIALIZE VARIABLES
        left = right = 0
        curr_sum = 0
        ans = float('inf')

        #START IMPLEMENTING THE SLIDING WINDOW
        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target: #now we have a valid subarray shrink the window to get the minimal

                ans = min(ans, right - left + 1) # it checks if it is minimal while the subarray is valid

                curr_sum -= nums[left]
                left += 1

            

        return ans if ans != float('inf') else 0
            
