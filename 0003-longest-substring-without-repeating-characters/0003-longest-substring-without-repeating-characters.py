class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        PSEUDOCODEE
        init sliding window
        as right moves through the window add to the set
        while s[right] in set:
            remove s[left] from set
            increment left
        calculate the length of valid sliding window

        """

        left = ans = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans

    #Time and Space Complexity = O(n)