"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sched = []  # will contain a tuple of start/end time and 1(start)/-1(end) that indicates num of room being occupied
        for i in intervals:
            sched.append((i.start, 1))
            sched.append((i.end, -1))
        
        # sort by time first and then by room occupied
        sched.sort(key=lambda i: (i[0], i[1]))

        # maxRoomCount = max. number of rooms being used simultaneously ==> min. number of meeting rooms needed
        # activeRoomCount = running counter for actively used rooms 
        maxRoomCount = activeRoomCount = 0
        for s in sched:
            activeRoomCount += s[1]
            maxRoomCount = max(maxRoomCount, activeRoomCount)
        
        return maxRoomCount

# Greedy Solution
