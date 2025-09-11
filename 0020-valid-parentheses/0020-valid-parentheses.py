class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "[":"]", "{":"}"}
        stack = []

        for ch in s:
            if ch in brackets:
                stack.append(ch)
                continue
            # print(stack)

            if stack and brackets[stack[-1]] == ch:
                stack.pop()
            else:
                return False


        return not stack

        #Space Complexity: O(n)
        #Time Complexity: O(n)