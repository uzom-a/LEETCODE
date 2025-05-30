class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    res.append(tuple([i,j]))

        return len(res)

        """
        I skipped pseudocode time and I don't know the time or space complexity let chatgpt help me
        Time complexity = O(n)^2
        Space Complexty = O(n)^2
        """
