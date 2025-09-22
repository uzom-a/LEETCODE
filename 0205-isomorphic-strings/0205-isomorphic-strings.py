class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        dict_track = {}
        mapped_chars = set()

        while i < len(s) and j < len(s):
            if s[i] in dict_track:
                if dict_track[s[i]] != t[j]:
                    return False #break the while loop and flag the error
            else:
                if t[j] in mapped_chars:
                    return False #we don't need two letters mapping to one
                dict_track[s[i]] = t[j]
                mapped_chars.add(t[j])

            i += 1
            j += 1
        
        return True #if we have reached this stage then no issues it is an isomorphic string

# Space Complexity: O(n)
# Time Complexity : O(n) since both strings are of equal length