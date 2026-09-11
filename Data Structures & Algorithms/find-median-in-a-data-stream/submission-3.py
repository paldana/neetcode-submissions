from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        # self.small - max heap --> largest at the leftmost
        # self.large - min heap --> smallest at the leftmost
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, num * -1)    # -1 because max heap

        ## rebalance the heaps - have buffer +/- 1
        # if small is bigger than large by more than 1, transfer current largest num in maxHeap to minHeap (large)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        # vice versa
        elif len(self.small) + 1 < len(self.large):
            val = heappop(self.large)
            heappush(self.small, val * -1)

            

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # return the largest value in maxHeap as the median
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:   # if equal, get largest num from maxHeap and smallest num from minHeap
            return ((self.small[0] * -1) + self.large[0]) / 2.0
        