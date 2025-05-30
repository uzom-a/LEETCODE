class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def char_count(s): #we need a function to check the static freq that's why we are using a fixed array
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            return count

        s1_count = char_count(s1)

        windowcount = char_count(s2[0:len(s1)]) #the first fixed subarray
        if s1_count == windowcount:
            return True

        for i in range(len(s1), len(s2)): #start from the next sliding window
            windowcount[ord(s2[i-len(s1)]) - ord('a')] -= 1 #remove the left
            windowcount[ord(s2[i]) - ord('a')] += 1 #move to the right

            if s1_count == windowcount:
                return True

        return False

        """
        Time Complexity is O(n)
        I think Space Complexity is O(1) because the both windows have a fixed size of 26 characters
        """
