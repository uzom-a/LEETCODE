class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_1 = set(nums1)
        minn = float('inf')
        for num in nums2:
            if num in set_1 and num < minn:
                minn = num
        if minn == float('inf'):
            return -1
        return minn 