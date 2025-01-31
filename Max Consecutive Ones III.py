class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        maximum = 0
        n = len(nums)

        for r, num in enumerate(nums):
            if not num: #aspa if it is 0
                while k <= 0:
                    if nums[l] == 0:
                        k += 1
                    l += 1
                else:
                    k -= 1
            
            maximum = max(maximum, r - l + 1)

        return maximum

        """
        U-Understand
        find the greatest consecutivenumber of 1s after reducing k  to -1

        M-Match
        dynamic sliding window? Yes, this approach is using a dynamic sliding window    technique12. In a dynamic sliding window, the size of the window can vary based on certain conditions, 

        P-Plan

        I-Implement
        look above

        R-Review

        E-Evaluate
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
