class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #using the AP sum formula to have an O(1)space complexity
        n = len(nums)
        #the sum for AP formula is (first term + last term )/2 times the number of terms
        #the number of terms is (n + 1) because we are counting 0
        total = n*(n+1) // 2


        return total - sum(nums)
