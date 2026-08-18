from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        nR, nC = len(grid), len(grid[0])
        visited = set()     # will contain visited (r,c)
        q = deque()
        numIslands = 0
        
        # perform BFS to check adjacent cells to determine the number of islands
        def bfs(row, col):
            q.append((row,col))
            visited.add((row,col))

            while q:
                r, c = q.popleft()
                dirs = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr, dc in dirs:
                    newRow, newCol = r + dr, c + dc
                    if (newRow in range(nR) and
                        newCol in range(nC) and
                        grid[newRow][newCol] == "1" and
                        (newRow, newCol) not in visited):
                        visited.add((newRow, newCol))
                        q.append((newRow, newCol))                

        for r in range(nR):
            for c in range(nC):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    numIslands += 1
        
        return numIslands


        