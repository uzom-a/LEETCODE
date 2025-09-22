class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        #O(n log n ) time complexity 
        #O(n) space complexity  because the sorted() function returns a new list

