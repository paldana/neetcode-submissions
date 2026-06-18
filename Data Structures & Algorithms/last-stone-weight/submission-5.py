class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Heap Solution
        if len(stones) == 1:
            return stones[0]
        # Do a maxHeap so the bigger values are at the top, but in -
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            s1, s2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            if s1 == s2: 
                continue

            heapq.heappush(maxHeap, -max(s1-s2, s2-s1))
            heapq.heapify(maxHeap)

        return -maxHeap[0] if maxHeap else 0


            