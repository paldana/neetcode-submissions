## BFS Approach
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        # q = deque()
        
        def bfs(row, col):
            q = deque([(row,col)])    
            # q.append((row,col))
            visited.add((row, col))
            while q:
                r, c = q.popleft() 
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        (nr,nc) not in visited and
                        grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
    
        return islands