class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: 
            return word
        help_str = ""
        for i in range(len(word)):
            if word[i] != ch:
                help_str = help_str + word[i]
            if word[i] == ch:
                help_str = help_str + word[i]
                break
        return help_str[::-1] + word[i+ 1:]