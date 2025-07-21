class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        PSEUDOCODE
        -init stack
        -init count to 1
        -loop through the string 
        -if stack and stack[-1] == ch
            -count ++
        - if stack and stack[-1] != ch:
            -count = 1
        -if count >= 3:
            continue
        -else:
            stack.append(ch)

        """

        stack = []
        count = 1

        for ch in s:
            if stack and stack[-1] == ch:
                count += 1
            if stack and stack[-1] != ch:
                count = 1

            if count >= 3:
                continue
            else:
                stack.append(ch)
        # print(stack)
        return ''.join(stack)

        # Time Complexity: O(n)
        # Space Complexity: O(n)