class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_p = 0
        t_p = 0

        if s == "":
            return True

        for t_p in range(len(t)):
            if s[s_p] == t[t_p] and s_p < len(s):
                s_p += 1
                t_p += 1
                if s_p == len(s):
                    return True
            else:
                t_p += 1
            
        if s_p == len(s):
            return True
        else:
            return False
"""
U-Understand:

find the occurence of s in t 
make sure it follows sequential order

M-Match: two pointers, string

P-Plan:

create a pointer for t 
create a pointer for s

check through t if s is in t
if yes, move the pointer for s  and  the pointer for t
if no, move the pointer for t only

if we reach the end of s then return true
if the t pointer is at the end and s pointer has not finished then return False

I-Implement:
look above

R-Review

E-Evaluate
Time complexity : O(n)
Space Complexity : O(1)

"""
        
