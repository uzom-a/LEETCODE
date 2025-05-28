from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        count = counter(nums)
        iterate through the dictionary
            get the max frequency
        iterate through the dictionary again and add the frequency of elements with max frequency
        """

        count = Counter(nums)
        ans = 0
        max_freq = 0

        for value in count.values():
            max_freq = max(max_freq, value)

        for key, value in count.items():
            if value == max_freq:
                ans += value

        return ans

        #time complexity = O(n)
        #space complexity = O(n)
