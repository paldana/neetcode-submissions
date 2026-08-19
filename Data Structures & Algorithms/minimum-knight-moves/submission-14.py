from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        DIRECTIONS = [(1,2), (2,1), (-1,2), (-2,1),
                      (1,-2), (2,-1), (-1,-2), (-2,-1)]

        def bfs(x,y):
            ## cleaner version in initializing sets and deque with the initial position of knight
            visited = {(0, 0)}      
            q = deque([(0, 0)])     
            moves = 0
            while q:    
                for _ in range(len(q)):     # run a loop at the current move level 
                    kX, kY = q.popleft()
                    # print(f"{moves=} | {kX=} | {kY=}")
                    if (kX, kY) == (x, y):
                        return moves
                    
                    for dx, dy in DIRECTIONS:
                        nx, ny = kX + dx, kY + dy
                        if (nx, ny) not in visited:   
                            q.append((nx, ny))
                            visited.add((nx, ny))
                            
                moves += 1  # only increment after each level

        return bfs(x, y)

## Personal Solution attempt - BFSish -- timing out?