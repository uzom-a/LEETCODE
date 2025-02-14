class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = []
        i = 0

        while i < n:
            #reverse the chunk

            chunk = s[i:i+k]
            res.append(chunk[::-1])

            #add the rest unchanged
            res.append(s[i+k:i+2*k])
            
            #get the next chunk
            i = i + 2*k

        return "".join(res)

        """
        Space Complexity - O(n)
        Time Complexity - O(n)
        """
            
        
