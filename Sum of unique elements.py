class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        ans = 0

        for num in nums:
            seen[num] += 1

        for key, value in seen.items():
            if value > 1:
                continue
            else:
                ans += key

        return ans

        "Time cOMPLEXITY = O(n).  Space complexity = O(n)"
