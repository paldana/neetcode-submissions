## Sweep Line Algorithm
# Time: O(n+m * log(n+m))
# Space: O(n+m)
# where m is len(queries) and n is len(intervals)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        events = []
        # Create events for intervals 
        # (start/end time, type, length of interval, index) 
        # type: 0 - start, 1 - query, 2 - end
        for idx, (start, end) in enumerate(intervals):
            events.append((start, 0, end - start + 1, idx))
            events.append((end, 2, end - start + 1, idx))

        # Create events for queries
        # (query, type, index)
        for i, q in enumerate(queries):
            events.append((q, 1, i))

        # Sort by time and type (end before query)
        events.sort(key=lambda x: (x[0], x[1]))

        # Min heap storing [size, index]
        sizes = []              # (interval_length, interval_index)
        ans = [-1] * len(queries)
        inactive = [False] * len(intervals)

        for time, type, *rest in events:    ## *rest gets the remaining values of list since interval events have 4 total, while queries events only has 3. Using this method, we'll be able to dynamically extract the values appended from above.
            if type == 0:  # Interval start
                interval_size, idx = rest
                heapq.heappush(sizes, (interval_size, idx))
            elif type == 2: #Interval end
                idx = rest[1]
                inactive[idx] = True
            else: # Query. -- not sure what's the while loop for...
                query_idx = rest[0]
                while sizes and inactive[sizes[0][1]]:
                    heapq.heappop(sizes)
                if sizes:
                    ans[query_idx] = sizes[0][0]

        return ans

