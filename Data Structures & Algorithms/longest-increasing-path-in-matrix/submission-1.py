## Dynamic Programming - Top-Down - Memoization x Recursion
# Time and Space: O(m x n) 
#   where m and n are lengths of row and col of the matrix
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}  # Key: (r,c), Value: LongestIncreasingPath (LIP)

        def dfs(r, c, prevVal):
            # base case - check if current cell is within range and value is greater than the previous cell's value
            if (r not in range(ROWS) or
               c not in range(COLS) or 
               matrix[r][c] <= prevVal):
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            res = 1  # each cell will always have 1 LIP by default
            moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in moves:
                # get the max LIP you can get after recursing the neighboring cells
                # +1 is for the current cell (r,c)
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))

            memo[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(memo.values())