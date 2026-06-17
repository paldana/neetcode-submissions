class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(nums)
        #maintain K number of integers in the heapify
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)   # add new value to the heap

        # check if heap contains K number of integers
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)     # pop the smaller values from the heap 
        
        return self.minHeap[0]          # this will contain the Kth largest element

    
    # Min Heap Solution
    # Time and Space Complexity: O(1)

