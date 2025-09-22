class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower().replace(" ", "")
        s = "".join(ch for ch in s if ch.isalnum())
        # print(s)
        
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

        #Time Complexity = O(n)
        #Space Complexity = O(n)