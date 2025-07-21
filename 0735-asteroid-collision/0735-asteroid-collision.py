class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        PSEUDOCODE
        -create stack
        -add a positive asteroid to stack
        -if a negative asteroid is encountered check with the top of the stack and pop the smaller one
        -return stack
        """

        stack = [asteroids[0]]
        
        for num in asteroids[1:]:
            flag = False
            while stack and stack[-1] > 0 and num < 0 and not flag:
                flag = abs(num) <= stack[-1]
                if abs(num) < stack[-1]:
                    break
                stack.pop()
                  
            if not flag:
                stack.append(num)    
                
        return stack
        # Time Complexity: O(n)
        # Space Complexity: O(n) where n is the number of asteroids