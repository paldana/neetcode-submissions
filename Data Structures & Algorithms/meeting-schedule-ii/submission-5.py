"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startList = sorted([i.start for i in intervals])
        endList = sorted([i.end for i in intervals])
        
        # count will be the number of rooms in use at the same time
        # res will be the max amount of rooms being used simultaneously
        res = count = 0
        s = e = 0       # pointers for the start and end lists
        while s < len(startList):
            if startList[s] < endList[e]:
                s+=1
                count += 1
            else:
                # endList[e] > startList[s]
                e += 1
                count -= 1
            res = max(res, count)
        return res