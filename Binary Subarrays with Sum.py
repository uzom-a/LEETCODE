class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Try to use a hashmap and a prefix sum because we want current sum that equals goal
        """

        total_count = 0
        current_sum = 0
        freq = {}
        freq[0] = 1 #a prefix sum that starts with 0 would have one freq in the d

        for num in nums:
            current_sum += num
           
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]

            if current_sum in freq:
                freq[current_sum] += 1
            else:
                freq[current_sum] = 1

        return total_count

        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
    
