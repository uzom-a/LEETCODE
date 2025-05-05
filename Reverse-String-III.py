class Solution:
    def reverseWords(self, s: str) -> str:
        """
        U-Understand
        reverse each word in the string of strings

        M-Match
        two pointers, string

        P-Plan
        change the given string to a list using the split method
        create an answer list
        reverse each word in the list
        append the word to the answer list

        I-Implement
        look below
        """

        result = s.split(" ")
        n = len(result)
        answer = []
        
        for i in range(n):
            word = result[i]
            word = word[::-1]
            answer.append(word) #append the reversed word to the list
            answer.append(" ") #append a space after each word

        final_string = "".join(answer)
        final = final_string.rstrip()

        return final

        """
        R-Review
        this should work well

        E-Evaluate
        Time Complexity : O(n) I thought it was O(n)^2 tbh
        Space Complexity: O(n)
        """




        
