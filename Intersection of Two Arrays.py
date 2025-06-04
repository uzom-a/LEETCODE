class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums2)
        output = set() #we need the unique elements without their duplicates

        for num in nums1:
            if num in seen: #using a set because it is O(1) operation
                output.add(num)

        return list(output) #the output needs to be in a list

#Time Complexity is O(n + m) where n stands for the length in nums1 and m is the length of the set which is created from nums2
#Space Complexity is O(m + k) where k is the number of unique integers in the output and m is the length of the set that is created from nums2
