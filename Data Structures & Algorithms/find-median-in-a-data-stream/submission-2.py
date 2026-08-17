import heapq


class MedianFinder:
    def __init__(self):
        # self.small = maxHeap => large values at the beginning of list, just negated
        # self.large = minHeap => small values at the beginning of list
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        ## begin by adding new num to the small list first
        if self.large and num > self.large[0]:
            # add new val in the large list
            heapq.heappush(self.large, num)
        else:  # add new val in the small list
            heapq.heappush(self.small, num * -1)

        ## Rebalance the two heap lists - have a buffer of +/- 1 between the two
        if len(self.small) > len(self.large) + 1:
            # move the largest value in the small heap to the large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            # move smallest value from the large heap to the small heap
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        # find the median depending on the combined number of values from both heaps
        if len(self.small) > len(self.large):
            # return largest value in the small heap
            return float(-1 * self.small[0])
        elif len(self.small) < len(self.large):
            return float(self.large[0])
        else:  # even number of values for both heaps
            return ((-1 * self.small[0]) + self.large[0]) / 2.0
