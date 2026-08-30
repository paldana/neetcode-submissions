from heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []    # list of tuples - (dist from origin, [x,y])
        for p in points:
            x, y = p[0], p[1]
            dist = math.sqrt(x**2 + y**2)       # Make sure you use the correct python operands! ^ is for XOR bit operations, ** is the power operator
            heapq.heappush(minHeap, (dist,[x,y]))
        
        print(minHeap)
        res = []
        for _ in range(k):
            _, pts = heapq.heappop(minHeap)

            res.append(pts)
        
        return res

