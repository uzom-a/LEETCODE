from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(open: int, close: int, current: str):
            if open == 0 and close == 0:
                result.append(current)
                return

            if open > 0:
                generate(open - 1, close, current + '(')

            if close > open:
                generate(open, close - 1, current + ')')

        generate(n, n, "")
        return result
