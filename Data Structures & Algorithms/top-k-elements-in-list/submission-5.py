from collections import Counter
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sorting Approach
        freqMap = Counter(nums)

        freq = []
        for num, cnt in freqMap.items():
            freq.append((cnt, num))
        freq.sort(reverse=True)
    
        res = []
        for i in range(k):
            res.append(freq[i][1])
        return res

        # MinHeap Approach

        # Bucket Sort Approach - Optimal