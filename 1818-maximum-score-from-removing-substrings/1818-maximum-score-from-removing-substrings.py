class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # x --> "ab"
        # y --> "ba"

        """
        PSEUDOCODE
        -init stack
        -init score
        -if x is higher than or equal to y then start with x
            -loop through s 
                -if encountered a "b" and stack[-1] is "a" #ab
                    -pop from stack
                    -score += x
                else:
                    stack.append(ch)

            leftover = []
            for ch in stack
                then do for ba
        -else:
            do the reverse
        return score
        """

        stack = []
        score = 0

        if x >= y:
            for ch in s:
                if stack and ch == "b" and stack[-1] == "a":
                    score += x
                    stack.pop()
                else:
                    stack.append(ch)
            
            leftover = []
            for ch in stack:
                if leftover and ch == "a" and leftover[-1] == "b":
                    score += y
                    leftover.pop()
                else:
                    leftover.append(ch)
        else:
            for ch in s:
                if stack and ch == "a" and stack[-1] == "b":
                    score += y
                    stack.pop()
                else:
                    stack.append(ch)

            leftover = []
            for ch in stack:
                if leftover and ch == "b" and leftover[-1] == "a":
                    score += x
                    leftover.pop()
                else:
                    leftover.append(ch)

        return score

        """
        Takeaway:
        You are still simulating the two operations but you start the first for loop from the higher point and the second for loop would stem from the lower point's remnants

        Time Complexity: O(n)
        Space Complexity: O(n)
        """