import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Heap Solution
        # We can create a tuple of (dist from origin, [xi, yi]) and save it into a minHeap.
        # Then we'll get k smallest distance from the heap, get the respective coordinates,
        # and save them all in a list.

        # first, we calculate the distance from each points
        # dist = sqrt(x^2 + y^2)
        minHeap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            minHeap.append((dist, [x,y]))
        
        heapq.heapify(minHeap)
        
        # retrieve the k coordinates of the closest points to the origin
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res


# Time Complexity: O(n+k∗logn) when building the heap with heapify, or 
#                  O(n∗logn+k∗logn) when inserting each point with a heap push.
# Space Complexity: O(n)