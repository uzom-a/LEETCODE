class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols -1

        while row < rows and col >= 0:
            curr = matrix[row][col]

            if curr == target:
                return True
            elif target < curr:
                col -= 1 #move left
            else:
                row += 1 #move down

        return False