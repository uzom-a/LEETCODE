class Solution:
    def possibleStringCount(self, word: str) -> int:
        length = 1 #because the OG word might have been what Alice wanted
        i = 0
        #abbcccc
        #     i
        #count = 3 


        while i < len(word):
            count = 0
            while i + 1 < len(word) and word[i] == word[i + 1]:
                count += 1 #so I am only keeping track of extras
                i += 1

            if count >= 1:
                length += (count)

            i += 1

        return length

        #Time Complexity is O(n)  #I only go through the string once
        #Space Complexity is O(1)
        """
        next time, only keep track of extras 
        it makes more sense to the problem of alice's keyboard anyways
        """