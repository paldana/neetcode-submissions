from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        DIRECTIONS = [(1,2), (2,1), (-1,2), (-2,1),
                      (1,-2), (2,-1), (-1,-2), (-2,-1)]

        def bfs(x,y):
            visited = set()
            q = deque()             # will consist of a tuple - (numMoves taken to get knight to current position, current Kx, current Ky)
            q.append((0, 0, 0))     # if current coordinates of Knight is provided as an input, update initial values of Kx and Ky
            
            while q:    
                for _ in range(len(q)):
                    moves, kX, kY = q.popleft()
                    # print(f"{moves=} | {kX=} | {kY=}")
                    if (kX, kY) == (x, y):
                        return moves
                    
                    # visited.add((kX,kY))

                    for dx, dy in DIRECTIONS:
                        nx, ny = kX + dx, kY + dy

                        if (nx, ny) not in visited:   
                            q.append((moves + 1, nx, ny))
                            visited.add((nx, ny))
                    
        return bfs(x, y)

## Personal Solution attempt - BFSish -- timing out?