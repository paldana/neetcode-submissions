class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nROWS, nCOLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # find treasure cells first and add them to queue
        for r in range(nROWS):
            for c in range(nCOLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        # starting from the treasure cells, go through neighboring
        # land cells to add number of steps on the cells in one pass
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = steps

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (nr in range(nROWS) and
                        nc in range(nCOLS) and
                        (nr, nc) not in visited and
                        grid[nr][nc] != -1):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            steps += 1      # increase steps after each breadth level
