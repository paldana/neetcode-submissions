"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ## Sweep Line Algorithm
        meetingsMap = defaultdict(int)    # key: start/end time, val: rooms occupied - +1 for start /-1 for end

        for i in intervals:
            meetingsMap[i.start] += 1
            meetingsMap[i.end] -= 1
        
        activeRooms = 0
        maxRoomOccupied = 0
        # print(f"{meetingsMap=} | {meetingsMap.keys()=}")
        for m in sorted(meetingsMap.keys()):    # needs to be sorted - otherwise, max occupied will always be 1 as we go through the map - +1, -1, +1, -1, ...
            activeRooms += meetingsMap[m]    # get the number of rooms occupied per time
            maxRoomOccupied = max(maxRoomOccupied, activeRooms)
        
        return maxRoomOccupied