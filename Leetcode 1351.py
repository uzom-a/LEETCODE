# Count negative numbers in a sorted matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #REMEMBER DECREASING ORDER THAT IS HOW TO ACHIEVE THIS APPROACH

        n = len(grid[0]) #length of columns
        m = len(grid) #length of rows
        count = 0
        row = m - 1 # we are starting from bottom left look at the structure of the grid
        col = 0 # we are starting from bottom left look at the structure of the grid

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += (n-col)  #Count all negative numbers in this row
                row -= 1 # move up the grid
            else:
                col += 1 #move to the right if positive to check all the elements in that row are positive
        
        return count

        #TIME COMPLEXITY = O(n+m)
        #SPACE COMPLEXITY = O(1)

        """count = 0

        for sublist in grid:
            for item in sublist:
                if item < 0:
                    count += 1
                    
        return count

        #Time complexity: O(m * n)
        #Space complexity: O(n)
        """
