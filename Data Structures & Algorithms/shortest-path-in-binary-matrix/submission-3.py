## Bidirectional BFS - practice attempt
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        
        if N == 1:      # if 1x1 matrix
            return 1
        
        # setup two queues that will start from the start and end
        q1 = deque([(0,0)])
        q2 = deque([(N-1, N-1)])
        start, end = -1, -2
        grid[0][0] = start
        grid[N-1][N-1] = end
        dist = 2        # 1 on both ends

        moves = [(0,1), (1,0), (1,1), (1,-1),
                (0,-1), (-1,0), (-1,1), (-1,-1)]

        while q1 and q2:
            for _ in range(len(q1)):
                r, c = q1.popleft()

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc

                    if (nr in range(N) and
                        nc in range(N)):
                        
                        if grid[nr][nc] == end:
                            return dist
                        
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = start
                            q1.append((nr,nc))
            
            # swap the two queues
            q1, q2 = q2, q1
            start, end = end, start
            dist += 1
        
        return -1


                        

                