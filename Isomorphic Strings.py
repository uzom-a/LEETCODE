# Time Complexity : O(n^2)
# Space Complexity : O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx)) #record the index by first occurence
        for idx in t:
            map2.append(t.index(idx)) #record the index by first occurence
        if map1 == map2:
            return True
        return False
