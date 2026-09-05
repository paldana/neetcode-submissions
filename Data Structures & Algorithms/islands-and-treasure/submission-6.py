class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nROWS, nCOLS = len(grid), len(grid[0])
        visited = set()
        q = deque()  # will initially contain the (r,c) of the treasure cells
        # then the land
        INF = 2147483647  # Given value

        # look for the cells containing the treasures
        for r in range(nROWS):
            for c in range(nCOLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))

        steps = 0
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = steps

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (nr in range(nROWS) and
                        nc in range(nCOLS) and 
                        (nr,nc) not in visited and
                        grid[nr][nc] != -1 ):
                        visited.add((nr, nc))
                        q.append((nr,nc))

            steps += 1
        
        return

