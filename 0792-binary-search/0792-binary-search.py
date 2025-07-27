class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                


        return -1