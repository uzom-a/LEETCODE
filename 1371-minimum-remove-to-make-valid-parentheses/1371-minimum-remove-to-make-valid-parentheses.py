class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        for i , ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop() #because it's balanced so no need to discard this pair
                else: #that means the stack is empty early
                    s[i] = ""

        while stack: #if there are still stuff in the stack
            s[stack.pop()] = ""

        return "".join(s) #make everything a string again which will close the empty / invalid parentheses