class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m -1 
        y = n -1

        for z in range(m + n - 1, - 1, -1):  #we are looping backwards
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
            elif y < 0:
                break #this means we are basically done with the nums2
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1

        "Time Complexity = O(n+m)"
        "Space Complexity: 0(1)"
