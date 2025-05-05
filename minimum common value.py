class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        #use the two pointer approach for two arrays

        #INITIALIZE VARIABLES
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]: #so that the pointer i would catch up
                i += 1
            else:
                j += 1

        return -1
        
