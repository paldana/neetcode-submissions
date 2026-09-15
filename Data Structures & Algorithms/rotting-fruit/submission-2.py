from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        freshFruits = 0
        q = deque()

        # go through the grid and find the number of fresh fruits and positions of the rotten ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruits += 1
                elif grid[r][c] == 2:
                    visited.add((r, c))
                    q.append((r, c))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0
        # go through the grid again and start visiting adjacent nodes starting from the rotten fruits
        # every layer of the BFS will be a minute -- keep iterating while there are fresh fruits remaining
        while freshFruits > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        freshFruits -= 1

            minutes += 1    # increment minutes after every complete iteration of for-loop (BFS layer)

        return minutes if freshFruits == 0 else -1