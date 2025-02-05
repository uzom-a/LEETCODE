class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        occurences = {}
        for letter in s1:
            if letter in occurences:
                occurences[letter] += 1
            else:
                occurences[letter] = 1

        occ2 = {}
        for letter2 in s2:
            if letter2 in occ2:
                occ2[letter2] += 1
            else:
                occ2[letter2] = 1
        i = 0
        k = 0
        count = 0
        while i < len(s1) and k < len(s2):
            if s1[i] == s2[k]:
                k += 1
                i += 1
            else:
                count += 1
                k += 1
                i += 1
            
            if count > 2:
                return False

        if occurences == occ2:
            return True
        else:
            return False

    """
    U-Understand
    you need to check the number of occurences of a letter that they are equal in both strings and ensure the different indices are just 2 and nothing more

    M-Match
    strings, two pointers

    P-Plan
    iterate through and create a dictionary of the occurences for both letters
    check that the number of different indices are 2 or less

    I-Implement 
    look at the code above

    R-Review
    
    E-Evaluate
    Time Complexity: O(n)
    Space Complexity : O(n)
    """


        
