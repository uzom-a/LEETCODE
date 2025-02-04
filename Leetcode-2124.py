class Solution:
    def checkString(self, s: str) -> bool:
        return s == ''.join(sorted(s))

    """
    U-Understand
    we need to make sure all the 'a's are placed before the b 

    M-Match
    strings
    sorting

    P-Plan
    sort the og string
    copare the new sorted string to the og string
    return boolean value

    I-Implement
    look at code above

    R-Review
    we code definitely do this in O(1) complexity compared to O(n logn)
    
    E-Evaluate
    Time Complexity : O(n logn )
    Space complexity : O(n)

    """
