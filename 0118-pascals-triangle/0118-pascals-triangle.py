class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows

        if n == 0:
            return []
        if n == 1:
            return [[1]]

        n = numRows - 2

        result = [[1], [1,1]]
        element = 1
        
        while n:
            first = 0
            second = 1
            #beginning of new row
            result.append([1])

            #building the current row
            while second < len(result[element]):
                result[element+1].append(result[element][first] + result[element][second])
                first += 1
                second += 1
            result[element+1].append(1)

            #preparing for the next iteration
            element += 1
            n -= 1

        return result

"""
Time Complexity = O(n^2)
Space Complexity = O(n^2)
"""