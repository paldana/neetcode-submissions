import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = nums
        heapq.heapify(self.maxHeap)
        self.target = k

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)
        print(f"{self.maxHeap=}")
        print(f"{self.target} largest numbers")
        print(heapq.nlargest(self.target, self.maxHeap))

        return heapq.nlargest(self.target, self.maxHeap)[-1]
