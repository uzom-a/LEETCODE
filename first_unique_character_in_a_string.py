from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(list)

        for i, ch in enumerate(s):
            if ch in d:
                d[ch][0] += 1
            else:
                d[ch].append(1)
                d[ch].append(i)

        for val in d.values():
            if val[0] == 1:
                return val[1]

        return -1


'''
Time Complexity = O(n)
Space Complexity = O(n)

HOW TO CLEAN THE CODE:
get rid of examples comments 
1 > 2 > 3

fix variable names and function names

find 
get


'''
