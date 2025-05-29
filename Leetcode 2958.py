class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        PSEUDOCODE TIMEE
        intialize the pointers
        intialize the max_len
        intialize a count dictionary
        move though the sliding window with the right pointer
            if the window is invalid(i.e the count of an element is greater than k)
                increase the left pointer
            
            find the max_len while it is valid
        """
        left = max_len = 0

        count = defaultdict(int)

        for right in range(len(nums)):
            count[nums[right]] += 1
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
