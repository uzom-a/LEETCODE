from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #USE THE COUNTER TO GET THE COUNT OF ALL THE CHARACTERS
        count = Counter(text)
        
        b = count['b']
        a = count['a']
        l = count['l'] // 2 #this letter repeats itself twice so we need to divide by 2 to see the actual occurence in ballon
        o = count['o'] // 2 #same situation as l
        n = count['n'] 
        
        ans = min(b, a, l, o, n)
        
        return ans
