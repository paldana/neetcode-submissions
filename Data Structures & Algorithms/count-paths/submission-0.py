## Similar to problem: https://neetcode.io/problems/shortest-path-in-binary-matrix/question

## Dynamic Programming (Bottom-up x Space Optimized) - NeetCode's video solution
# Time: O(n * m)
# Space: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = row, n = cols
        # represents 1 row with n cols
        row = [1] * n           # this would be the bottow row where all cells are 1s 
                                # representing the number of moves available from that cell 
                                # (only to the right)

        # we're "simulating" that we're going through each row starting from the bottom
        # but really we're just adding cells to the right and below of the current cell 
        for i in range(m - 1):          
            newRow = [1] * n                # create each row and calculate using the values from the bottom row (currently "row")
            for j in range(n - 2, -1, -1):  # work in reverse starting from the 2nd to the right most column since the right most will cell will always be "1" - meaning only available move is down
                newRow[j] = newRow[j + 1] + row[j]  # add available moves from the right (using the updated moves from newRow[j+1]) and bottom cells (row[j])
            row = newRow                    # update the bottom row to the current newRow and repeat iteration until the m x n grid is complete
        return row[0]   # answer at the end will be the available moves from the top left corner (which is the first element of row by the end of the for-loops above)