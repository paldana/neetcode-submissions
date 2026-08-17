import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = [-s for s in stones]
        heapq.heapify(stonesHeap)
        print(f"Original list: {stonesHeap=}")
        while len(stonesHeap) >= 2:
            # heaviestStones = heapq.nlargest(2, stones)
            # s1, s2 = heaviestStones[0], heaviestStones[1]
            s1, s2 = heapq.heappop(stonesHeap), heapq.heappop(stonesHeap)
            print(f"{s1=} vs. {s2=}")
            if s1 < s2 or s1 > s2:
                newStone = abs(s2 - s1)
                heapq.heappush(stonesHeap, -newStone)
                print(f"{newStone=} added to heap -- updated {stonesHeap=}")
        
        return -stonesHeap[0] if stonesHeap else 0