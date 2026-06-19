class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Heap Solution
        # if len(stones) == 1:
        #     return stones[0]
        # Do a maxHeap so the bigger values are at the top, but in -
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            s1, s2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            if s1 == s2:        # if both stones are equal, they are destroyed
                continue

            heapq.heappush(maxHeap, -max(s1-s2, s2-s1))     # get the diff between 2 stones and push back to the heap
            # heapq.heapify(maxHeap)           # re-heapify the heap to keep the largest 2 stones up top for next cycle

        # return 0 if no stones were left in the heap or the value of the last stone
        return -maxHeap[0] if maxHeap else 0

# Time complexity: O(nlogn)
# Space complexity: O(n)