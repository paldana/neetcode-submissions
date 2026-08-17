import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # will contain tuple (dist from origin, (x,y))
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)   # (x - 0)^2 + (y - 0)^2
            heapq.heappush(minHeap, (dist,[x,y]))
        
        res = []
        for _ in range(k):
            d, coords = heapq.heappop(minHeap)
            res.append(coords)
        
        return res

