## Dynamic Programming - Top-Down - Memoization x Recursion
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}  # Key: (r,c), Value: LongestIncreasingPath (LIP)

        def dfs(r, c, prevVal):
            if (r not in range(ROWS) or
               c not in range(COLS) or 
               matrix[r][c] <= prevVal):
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            res = 1  # each cell will always have 1 LIP by default
            moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in moves:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))

            memo[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(memo.values())