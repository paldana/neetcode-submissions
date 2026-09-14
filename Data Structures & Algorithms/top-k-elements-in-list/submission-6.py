from collections import Counter
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Sorting Approach - Time: O(n log(n)), Space: O(n)
        # freqMap = Counter(nums)

        # freq = []
        # for num, cnt in freqMap.items():
        #     freq.append((cnt, num))
        # freq.sort(reverse=True)
    
        # res = []
        # for i in range(k):
        #     res.append(freq[i][1])
        # return res

        ## MinHeap Approach - Time: O(n*log(k)), Space: O(n)
        maxHeap = []
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        for num, cnt in freqMap.items():
            heappush(maxHeap, (-1 * cnt, num))

        res = []
        for _ in range(k):
            res.append(heappop(maxHeap)[1])
        return res




        ## Bucket Sort Approach - Optimal