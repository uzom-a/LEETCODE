class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        #brute force
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if i != j and j != k and i != k:
                        if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                            count += 1

        return count

        #Time and Sapce Complexity of O(n)^3 and O(1) respectively