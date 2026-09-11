from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        # small = maxHeap, large = minHeap
        self.small, self.large = [], [] 

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, num * -1)

        # balance both heaps - have a buffer +/- 1
        if len(self.small) > len(self.large) + 1:
            val = heappop(self.small) * -1
            heappush(self.large, val)
        elif len(self.small) + 1 < len(self.large):
            val = heappop(self.large)
            heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return ((self.small[0] * -1) + self.large[0])/2.0
        