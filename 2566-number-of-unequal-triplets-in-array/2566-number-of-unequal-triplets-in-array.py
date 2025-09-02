from collections import Counter
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        #optimized solution using their freq
        freq = Counter(nums)
        left = 0 #the numbers before that current number
        right = 0 #the remaining numbers
        n = len(nums)
        res = 0

        for val, count in freq.items():
            right = n - left - count

            res += left * right * count #multiplying because the choices are independent of each other picking something from left would not affect the next time that you are choosing a triplet sho get ni?
            left += count

        return res


        #Time Complexity is O(n)
        #Space Complexity is O(n)