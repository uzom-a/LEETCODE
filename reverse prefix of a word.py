class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        cut_out = word[0:i+1] 
        reverse = cut_out[::-1]

        ans = reverse + word[i+1:]

        return ans

