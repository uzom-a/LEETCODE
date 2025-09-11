from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        r_count = Counter(ransomNote)

        for key, val in r_count.items():
            if key not in magazine_count:
                return False

            if val > magazine_count[key]:
                return False
            
        return True

        # Space Complexity: O(n)
        # Time Complexity: O(n)