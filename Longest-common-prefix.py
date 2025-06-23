class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        PSEUDOCODE

        -find the shortest string in the array
        -use the letters of the first string to check other strings
        -if they are all the same letter at i add the letter to the stack
        -retur the common prefix

        Time Complexity : O(n*m) where n is the length of the array while m is the length of the shortest string
        Space Complexity is O(n)
        """

        i = 0
        min_length = float('inf')

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i] #not inclusive of i which is the bad part
            i += 1


        return s[:i] #incase everything worked out

        


