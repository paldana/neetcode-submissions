## BFS Practice
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)  # N x N matrix
        # base case - check if matrix has a valid path by checking start and end cells
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        moves = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]

        q = deque([(0, 0, 1)])  # r, c, length
        visited = set()
        while q:
            # for _ in range(len(q)):  # necessary?
            r, c, length = q.popleft()
            if [r, c] == [N - 1, N - 1]:
                return length

            # if (r,c) in visited:
            #     continue

            # visited.add((r,c))

            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                if (
                    nr in range(N)
                    and nc in range(N)
                    and (nr, nc) not in visited
                    and grid[nr][nc] == 0
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc, length + 1))
        
        return -1