## DFS using hash set approach
from collections import deque


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == 1:
                visited.add((r, c))
                currIsland.add((r - r_orig, c - c_orig))

                # go through neighboring nodes
                for dr, dc in moves:
                    dfs(r + dr, c + dc)
            else:
                return

        uniqueIslands = set()
        visited = set()  # will contain rows and columns that have been visited
        for r in range(ROWS):
            for c in range(COLS):
                currIsland = set()
                r_orig, c_orig = r, c
                dfs(r, c)
                if currIsland:
                    uniqueIslands.add(frozenset(currIsland))

        return len(uniqueIslands)
