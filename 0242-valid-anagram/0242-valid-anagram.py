class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for c in s:
            count[c] = count.get(c, 0) + 1

        # Subtract characters in t
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        # If all counts are zero, they are anagrams
        return True

    #O(n) Time Complexity
    #O(1) Space Complexity because it would store a constant number of 26