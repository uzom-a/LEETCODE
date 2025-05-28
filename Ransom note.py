class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(int)
        
        for char in ransomNote:
            d[char] += 1
            
        d2 = defaultdict(int)
        
        for char in magazine:
            d2[char] += 1
            
        for char in d:  #this iterates through only the keys
            if d[char] > d2[char]:
                return False
            
        return True
