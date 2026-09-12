class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                stack.pop()#the parenthesis is closed
            ans = max(ans, len(stack))
        return ans
             