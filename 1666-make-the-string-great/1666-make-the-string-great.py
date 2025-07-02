class Solution:
    def makeGood(self, s: str) -> str:
        if s == "":
            return s

        stack = []

        for ch in s:
            if stack and ( ch.lower() == stack[-1].lower() ) and (( ch.islower() and stack[-1].isupper() ) or ( ch.isupper() and stack[-1].islower())):
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
