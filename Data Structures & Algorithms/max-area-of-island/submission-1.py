from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                dirs = [(1,0),(0,1),(-1,0),(0,-1)]

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    # check if cell is not within range, water, or has been visited
                    if (nr not in range(ROWS) or 
                        nc not in range(COLS) or
                        grid[nr][nc] == 0 or
                        (nr,nc) in visited):
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr,nc))
                    area += 1

            return area


        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                   maxArea = max(maxArea, bfs(r,c))
        return maxArea 



## BFS Solution 
# Time and Space Complexity: O(m * n)
# Where m is the number of rows and n is the number of columns in the grid.