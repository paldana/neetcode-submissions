## BFS Solution

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # ROWS, COLS = len(grid), len(grid[0])  # can be simplified since we're given a BINARY matrix (n x n)
        n = len(grid)

        # edge case - check if the given grid has a valid path from top left to bottom right
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        moves = [(1, 0), (-1, 0), (1, 1), (-1, 1), 
                (-1, -1), (1, -1), (0, 1), (0, -1)]
        visited = set()
        q = deque([(0,0,1)])    # will contain r, c, and length of path

        while q:
            for _ in range(len(q)):
                r, c, length = q.popleft() 
                if r == (n-1) and c == (n-1):
                    return length

                visited.add((r,c))
                
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc

                    if (nr in range(n) and
                        nc in range(n) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 0 ):
                        q.append((nr, nc, length + 1))
                        visited.add((nr, nc))
        return -1

