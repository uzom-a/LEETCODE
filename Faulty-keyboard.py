class Solution:
    def finalString(self, s: str) -> str:
        """
        U-Understand

        reverse the characters before i 

        M-Match
        strings, array

        P-Plan 
        create a new list
        append characters to the list if current character is not i
        ekse: reverse the list 
        return list
        
        I-Implement 
        look below
        """

        result = []

        for i in range(len(s)):
            if s[i] == "i":
                result.reverse() #this takes O(n) time
            else:
                result.append(s[i])

        return "".join(result)

        """
        R-Review
        we need to look for a more optimal solution that I will submit soon

        E-Evaluate
        Time complexity is O(n^2)
        Space complexity is O(n)
        """

        
