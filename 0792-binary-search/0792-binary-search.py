class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        assign left and right
        use a while loop tht breaks when left > right
        find middle based on current left and right
        check if current middle position equals to target 
        if not move left or right based on equality sign
        else return
        """
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