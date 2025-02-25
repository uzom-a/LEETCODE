class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        U-Understand

        we need to find a word in that sentence that contains the search word
        if there is no word return - 1

        M-Match
        array, strings

        P-Plan
        split the sentence
        store the split words in a list
        iterate through the list
        check if any word in the list contains the search word at index 0
        if yes, return the index of that word in the list plus 1
        if the traversal is over return -1

        I-Implement
        look at the code below

        """

        listt = sentence.split(" ")
        
        for i in range(len(listt)):
            word = listt[i]
            if searchWord in word:
                index = word.find(searchWord)
                if index  == 0:
                    return i + 1

        return -1

        """
        R-Review
        I think you are finding the patterns while solving leetcode that is amazing!

        E-Evaluate
        Time Complexity -  O(k * m * l), where k is the number of words, m is the length of searchWord, and l is the length of each word in the sentence
        Space Complexity - O(n)
        """
