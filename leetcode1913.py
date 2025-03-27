class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest = float('-inf')
        second_largest = float('-inf')
        smallest = float('inf')
        second_smallest = float('inf')

        for i in range(len(nums)):
            if nums[i] > largest:
                second_largest = largest # make the second largest the former largest
                largest = nums[i]
            else:
                if nums[i] > second_largest:
                    second_largest = nums[i]

            if nums[i] < smallest:
                second_smallest = smallest # make the second smallest the former smallest
                smallest = nums[i]
            else:
                if nums[i] < second_smallest:
                    second_smallest = nums[i]

        return (largest * second_largest)  - (smallest * second_smallest)

        #Time complexity = O(n)
        #space complexity = O(1)
