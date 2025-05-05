class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #INTIALIZE VARIABLES
        vowels = set('aeiou')
        count = 0
        max_vowels = 0
        i = 0
        j = k

        #CREATE THE FIXED WINDOW
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_vowels = count

        #SLIDING WINDOW TECHNIQUE
        for i in range(k, len(s)):
            #remove the character left behind from the window
            if s[i-k] in vowels:
                count -= 1

            #add the new character to the sliding window
            if s[i] in vowels:
                count += 1

            max_vowels = max(max_vowels, count)

        return max_vowels
            
            
