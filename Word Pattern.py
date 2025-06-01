class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern): #base case
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, s):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        return True

        """
        a bijection is a one to one mapping so you have to make sure char maps to word and alsow word maps to char
        """

"""
Time Complexity = O(n)
Space Complexity = O(n)
"""
