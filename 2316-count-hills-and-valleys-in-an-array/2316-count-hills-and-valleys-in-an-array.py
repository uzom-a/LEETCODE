class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new = [nums[0]]#remove all adjacent duplicates while maintaining order
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                new.append(nums[i])

        # print(new)
        count = 0

        for i in range(1,len(new)-1):
            if new[i] < new[i-1] and new[i] < new[i+1]:
                count += 1
            elif new[i] > new[i-1] and new[i] > new[i+1]:
                count += 1
        return count

#Time Complexity: O(n)
#Space Complexity: O(n)