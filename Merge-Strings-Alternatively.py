class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        first = 0
        second = 0

        while first < len(word1) and second < len(word2):
            res += word1[first]
            first += 1
            
            if second < len(word2):
                res += word2[second]
                second += 1

        while first < len(word1): #append the remaining in first string because second is now out of bounds
            res += word1[first]
            first += 1

        while second < len(word2): #append the remaining in the second string because first is now out of bounds
            res += word2[second]
            second += 1

        return res


        """
        U-Understand
        merege the strings in alternating order

        M-Match 
        strings, two pointers

        P-Plan
        create new string
        create pointer for second array
        iterate through the array
        use the first pointer and add to the result string
        use the second pointer and add to the result string
        if left over in str1 or str2 apped to the end

        I-Implement
        look at the code above

        R-Review
        Handle the test case for the first string being longer than the second string

        E-Evaluate
        Time Complexity : O(n + m)
        Space Complexity : O(n + m)
        """
