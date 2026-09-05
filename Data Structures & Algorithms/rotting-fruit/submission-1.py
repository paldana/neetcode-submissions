from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ## Similar to the Walls and Gates / Islands and Treasures problem
        ## Multi Source BFS
        # Time and Space Complexity: O(m*n), where m = rows of grid, n = cols of grid
        nROWS, nCOLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fresh = 0

        # look for the cells where the rotten fruits are
        for r in range(nROWS):
            for c in range(nCOLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0
        # starting from the rotten fruits, go through the adjacent fruits using BFS
        # to determine how much
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                # grid[r][c] = minutes      # not necessary to update the cell's value

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (
                        nr in range(nROWS)
                        and nc in range(nCOLS)
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1
