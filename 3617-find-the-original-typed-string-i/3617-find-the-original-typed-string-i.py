class Solution:
    def possibleStringCount(self, word: str) -> int:
        #abbcccc
        n = len(word)
        i = 0
        total = 1 #original word typed out is correct

        while i < len(word):
            count = 1
            while i + 1 < n and word[i] == word[i+1]:
                count += 1
                i += 1
            if count >= 2:
                total += (count - 1)
            i += 1
                
        return total

        #O(n) --> time complexity
        #O(1) --> space complexity