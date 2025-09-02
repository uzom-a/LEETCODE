class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        list_of_words = s.split()
        return len(list_of_words[-1])
        # Time Complexity: O(n)
        # Space Complexity: O(n)