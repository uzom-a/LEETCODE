class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxx = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left) #normal height for a rectangle
            maxx = max(maxx, area)
            if height[left] < height[right]: #Move the shorter line inward to try to improve area 
                left += 1
            else:
                right -= 1

        return maxx

        # Time Complexity = O(n)
        # Space Complexity = O(1)