class Solution:
    def makeGood(self, s: str) -> str:
        """
-an empty stack
-traverse through the string
-for every character append to the stack
-if the new character we are about to append is .lower() or .upper() of the last character in the stack
  -pop the last character from the stack and don't current character to the stack
-return the string version of the stack

Time Complexity : O(n)
Space Complexity : O(n)
--> avoid nested if statements
"""
        stack = []

        for ch in s:
            if stack and ch.lower() == stack[-1].lower(): #to check if it is the same letter
                if (ch.isupper() and stack[-1].islower()) or (ch.islower() and stack[-1].isupper()): #to check if the cases are mismatched
                    stack.pop()
                    continue

            stack.append(ch)
        return ''.join(stack) 
            
