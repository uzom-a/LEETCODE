class Solution:
    def robotWithString(self, s: str) -> str:
        def smallest(right_freq): #to get the smallest character that is still available
            for i in range(26):
                if right_freq[i] > 0:
                    return chr(97 + i)
            return 'z'

        n = len(s)
        right_freq = [0] * 26  
        #for the line below, so that we can use indexing to order the characters alphabetically
        for c in s:
            right_freq[ord(c) - ord('a')] += 1

        t = []
        res = []
        pos = 0
        while pos < n:
            t.append(s[pos])
            right_freq[ord(s[pos]) - ord('a')] -= 1  #reduce the count since we encountered the letter

            while t and ord(t[-1]) <= ord(smallest(right_freq)):
                res.append(t.pop())
            pos += 1
        return ''.join(res)