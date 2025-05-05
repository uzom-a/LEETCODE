class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #INITIALIZE VARIABLES
        left = 0
        max_len = 0
        total_cost = 0
        
        #DYNAMIC SLIDING WINDOW
        for right in range(len(s)):
            total_cost += abs(ord(s[right])- ord(t[right])) #add the new character to the window

            while total_cost > maxCost: #when the subarray gives invalid
                total_cost -= abs(ord(s[left])-ord(t[left])) #remove a character so the window can slide
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

#time complexity = O(n)
#space complexity = O(1)
