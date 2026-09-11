from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.l = SortedList()
        
    def addNum(self, num: int) -> None:
        self.l.add(num) # amortize O(sqrt(n))
        
    def findMedian(self) -> float:  
        length = len(self.l)    
        if len(self.l) % 2 == 1:
            # odd
            return self.l[length // 2]
        else:
            # even
            left = self.l[length // 2 - 1]
            right = self.l[length // 2]
            return (left + right) / 2

