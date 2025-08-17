class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        PSEUDOCODE
        -add the first element to the stack
        -start iterating from the second element:
        -compare with the previous element in the stack
        -if they are the same then pop
        -else:
        -append the character to the stack
        -change the stack to a string and return

        """

        stack = [s[0]]
        for i in range(1,len(s)):
            if stack and (s[i] == stack[-1]):
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)

        #Time complexity = O(n)
        #Space Complexity = O(n)