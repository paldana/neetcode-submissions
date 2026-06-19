class MedianFinder:
    def __init__(self):
        # two heaps, large(minheap), small(maxheap)
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # check if the number of elements in the 2 heaps are ~same (+/- 1) 
        if len(self.small) > len(self.large) + 1:  # +1 is the allowance/buffer = ~same     
            val = -1 * heapq.heappop(self.small)   # if small heap way bigger than other heap,                                                 
            heapq.heappush(self.large, val)        # move the largest val from small to large heap 
        if len(self.large) > len(self.small) + 1:  # likewise if large is bigger than small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
        # removing and adding elements from heap - O(log (n))

    def findMedian(self) -> float:
        # get the median of the stream 
        # if the total number of elements is ODD, get the middle element of the combined heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        # if EVEN, get the biggest element in the small heap (maxHeap - largest at [0], just negated)
        # and add it with the smallest element from the large heap (minHeap - largest at [0])
        # and lastly, divide the sum by 2 to get the median
        return (-1 * self.small[0] + self.large[0]) / 2.0

# Heap Solution
# Time Complexity: O(m * log(n)) for addNum(), O(m) for findMedian()
# Space Complexity: O(n)
# -- where m is the number of function calls and n is the length of array