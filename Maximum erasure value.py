class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        PSEUDOCODE TIMEE
        create dynamic sliding window
        initialize max_sum
        create count set
        move through the nums array
            if num in set:
                increment left pointer and remove nums[left] from sum and remove nums[left] from set
            populate seen with nums[right]
            add nums[right] to maximum sum
            compare max_sums and keep the max
    
        return maximum length
        """

        left = 0
        max_sum = 0
        result = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                max_sum -= nums[left]
                left += 1 #you have to move after doing all those operations

            seen.add(nums[right])
            max_sum += nums[right]
            result = max(result,max_sum)

        return result

        """
        Time Complexity = O(n)
        Space Complexity = O(n) worst case
        """
