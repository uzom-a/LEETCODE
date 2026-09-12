class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        # for ch in s:
        #     if ch != stack[-1][0]:
        #         stack.append((ch,0))
        #     else:
        #         count = stack
        #         if count == k:
        #             stack.pop()
        #         stack.append((ch,count))

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        return "".join(char * num for char , num in stack)