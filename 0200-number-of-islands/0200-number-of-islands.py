class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs_iterative(r, c):
            stack = [(r, c)]
            while stack:
                row, col = stack.pop()
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                    grid[row][col] = "0"
                    stack.extend([(row+1, col), (row-1, col), (row, col+1), (row, col-1)])
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs_iterative(r,c)

        return islands

    #O(mxn) space and time complexity