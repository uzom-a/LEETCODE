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
                count += 1
                i += 1

            if count >= 1:
                length += (count)
            print(count)
            i += 1

        return length