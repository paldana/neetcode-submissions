## Hash By Local Coordinates Approach


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        unique_islands = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # base case - if r,c out of range, visited, or water
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            current_island.add((r - r_origin, c - c_origin))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                current_island = set()
                r_origin, c_origin = r, c  # will be used within dfs
                dfs(r, c)
                if current_island:
                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)
