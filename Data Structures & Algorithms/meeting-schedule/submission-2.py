"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sorting x 2 pointer approach
        intervals.sort(key=lambda i: i.start)    # sort by start time
        
        l, r = 0, 1
        while r < len(intervals):
            meeting1, meeting2 = intervals[l], intervals[r]
            # compare end time and start time of subsequent meetings
            if meeting1.end > meeting2.start:
                return False
            l, r = l + 1, r + 1
        
        return True

