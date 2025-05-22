class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen: #the while loop is the invalid window the left pointer is incremented in the while loop
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right-left+1)

        return ans
            
