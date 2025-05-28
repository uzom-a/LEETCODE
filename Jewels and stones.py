class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        d = defaultdict(int)
        d2 = defaultdict(int)
        
        for char in jewels:
            d[char] += 1
            
        for char in stones:
            d2[char] += 1  
            
        for char in d:
            if d[char] <= d2[char]:
                ans += d2[char]
                
        return ans
