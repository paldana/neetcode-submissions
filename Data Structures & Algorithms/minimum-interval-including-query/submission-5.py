import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()    # sort by start time    - O(n log(n))
        minHeap = []    # stores (interval length, end time)
        res = {}        # key: query, val: min. length for query
        i = 0

        for query in sorted(queries):
            # 1- store intervals in heap if their start time is less than query - potential to be in coverage
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))     # push qualified intervals to minHeap
                i += 1
            
            # once done with gathering all qualified intervals, we'll check for the shortest interval in the minHeap
            # that has the query, q, in its coverage
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            # store min. length in the res dict
            res[query] = minHeap[0][0] if minHeap else -1

        # after going through the sorted queries, need to create a list following the order of the original queries indexes
        return [res[q] for q in queries]
