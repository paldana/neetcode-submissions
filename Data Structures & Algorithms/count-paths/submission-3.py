## Dynamic Programming - Top-Down -- Memoization x Recursion
# Time and Space: O(m * n), where m and n are lengths of m and n, respectively
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a cache for the results of the dp
        memo = [[-1] * n for _ in range(m)]

        # find number of unique paths from each cell recursively
        def dfs(i, j):
            # base case 1 - check if we've reached the bottom right corner
            if i == (m - 1) and j == (n - 1):
                return 1  # 1 for the number of moves it will take
            # base case 2 - check if we're out of bounds
            if i >= m or j >= n:
                return 0
            # base case 3 - check if current i,j in memo
            if memo[i][j] != -1:
                return memo[i][j]

            # add resulting unique paths from bottom and right cells of the grid
            memo[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)
