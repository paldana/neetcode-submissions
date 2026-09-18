class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []        # ordedred by interval length - shortest interval at top (to be popped first)
        res = {}
        i = 0
        # Sort the queries, but keep their original order for the final answer by using "sorted(queries)"
        # "queries.sort()" will change the original queries ordering
        for q in sorted(queries):       
            ## 1- minHeap will store all the intervals that starts before q, regardless of end time
            # While there are intervals whose start ≤ q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]                      # l, r = start, end
                heapq.heappush(minHeap, (r - l + 1, r))  # push the interval length and end time to the heap
                i += 1

            ## 2- after getting the qualified intervals and adding to minHeap, check them and see if the end times, r (minHeap[x][1]), 
            ## are less than q. If they end before the q, pop it as q is not within that interval's coverage. O
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            # once we see an interval that q is in its coverage, it's the shortest length for that q, so store it in res
            res[q] = minHeap[0][0] if minHeap else -1
            
        return [res[q] for q in queries]    # using the queries original index, create an array with the values to be returned

## MinHeap Approach 
# Time: O(n log(n) + m log(m))
# Space: O(n+m)
# where m is len(queries) and n is len(intervals)