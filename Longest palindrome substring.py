class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l, max_r, maxx = 0, 0, 1
        n = len(s)
        for m in range(1, n):
            l2, r2 = m - 1, m
            l = m
            r = m
            while l - 1 >= 0 and r + 1 < n\
             and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            length = r - l + 1
            if length > maxx:
                maxx = length
                max_l = l
                max_r = r

            if s[l2] != s[r2]:
                continue

            while l2 - 1 >= 0 and r2 + 1 < n\
                and s[l2 - 1] == s[r2 + 1]:
                l2 -= 1
                r2 += 1

            length = r2 - l2 + 1
            if length > maxx:
                maxx = length
                max_l = l2
                max_r = r2
        
        return s[max_l:max_r+1]

"""
cbbd
l2 = 1
r2 = 2
m = 2
daBaba
0 2 4
aBaba
abaBa

n = 10**3
n ^ 2 -> 10^6

ppesduudsePP
     m 
l, r
save_l, save_r = l, r
t1hereSaRaccEcarh5ere
          m
r - l + 1
n ** 2
"""
