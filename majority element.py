class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_element = 0
        max_count = 0

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key, value in freq.items():
            if value > max_count:
                max_count = value
                max_element = key

        return max_element

        """
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
