class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]

        for num in gain:
            prefix.append(num + prefix[-1])

        # print(prefix)

        ans = max(prefix)

        return ans

        # time complexity = O(n)
        # space complexity = O(n)
