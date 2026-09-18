"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        minHeap = []     # will store meeting end times - len of this heap at the end will be the answer for number of max rooms needed

        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start: # meeting ends before start of current meeting
                heapq.heappop(minHeap)          # remove from heap to "free a room"
            heapq.heappush(minHeap, interval.end)
        
        return len(minHeap)
                

