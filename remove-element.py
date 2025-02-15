class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        j = 0    #pointer staying with the last occcurence of val
        
        for i in range(n):
            if nums[i] != val:
                nums[j] =nums[i]
                j += 1
        
        return j 



        "Time Complexity = O(n)"
        "Space Compleixty = O(1)"
