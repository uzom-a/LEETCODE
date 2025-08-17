class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        PSEUDOCODE
        -add any letter to the stack
        -if the current character is a backspace then pop from the stack
        -turn the stack into a list
        -check if the two are equal
        """

        def compare(word):
            stack = []
            for ch in word:
                if ch != "#":
                    stack.append(ch)
                else:
                    if stack:
                        stack.pop()
            return ''.join(stack)

        return compare(s) == compare(t)

        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """