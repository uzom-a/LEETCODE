class Solution:
    def removeStars(self, s: str) -> str:
        """
        PSEUDOCODE
        -add each character to the stack
        -if you encounter a star in the s string
            - then pop from the stack
        -join the stack and return
        """

        stack = []

        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                stack.pop()

        return "".join(stack)

        # Time Complexity = O(n)
        # Space Complexity = O(k)