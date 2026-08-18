from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        nRows, nCols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        q = deque()

        def bfs(r, c):
            visited.add((r,c))
            q.append((r,c))

            while q:
                # for _ in range(len(q)):
                row, col = q.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    # print(f"{nRows=} | {nCols=}")
                    # print(f"{newRow=} | {newCol=}")
                    # print(0< newRow < nRows)
                    # print(0< newCol < nCols)
                    
                    #if(newRow in range(nRows) and 
                    #   newCol in range(nCols) and
                    if(0 <= newRow < nRows and
                       0 <= newCol < nCols and
                       (newRow, newCol) not in visited and
                       grid[newRow][newCol] == "1"):
                        
                        visited.add((newRow, newCol))
                        q.append((newRow, newCol))


        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands