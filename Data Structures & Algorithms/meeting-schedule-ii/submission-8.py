"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)       # sort by start time
        min_heap = []                               # will store meeting end times

        for interval in intervals:
            # If the heap is not empty and the earliest end time (min_heap[0]) 
            # is less than or equal to the current meeting’s start
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)     # pop the top of the heap (reuse that room)

            # Push the current meeting’s end time into the heap (occupy a room).
            heapq.heappush(min_heap, interval.end)

        # the size of the heap represents the minimum number of rooms required
        return len(min_heap)
## Min-Heap Solution
# Time Complexity: O(n * log(n)) 
# Space Complexity: O(n)