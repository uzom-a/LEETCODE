class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5) + 1):
            z = (c - a**2) ** 0.5
            if z == int(z):
                return True

        return False
