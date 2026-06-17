class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = [-n for n in nums]
        heapq.heapify(self.maxHeap)      # negative values so largest number is first in list
        self.target = k

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, -val)      # add new val to heap as -
        print(f"Added new {val} in max heap: {self.maxHeap}")
        
        print(f"{self.target} largest elements:")
        print(heapq.nsmallest(self.target, self.maxHeap))
        # largest + value will be the smallest in the maxHeap;
        # return the Kth element (last in the nsmallest list) and correct the sign
        return -heapq.nsmallest(self.target, self.maxHeap)[-1]      
        
