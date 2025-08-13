class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #BASE CASE
        if n == 1:
            return True

        if n <= 0 or n % 3 != 0:
            return False

        #RECURSIVE CASE
        return self.isPowerOfThree(n/3)

       