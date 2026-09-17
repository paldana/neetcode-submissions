class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # binary search approach - personal attempt
        l, r = 0, len(intervals) - 1
        target = newInterval[0]

        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        # once out the while-loop, insert new interval where l is at
        intervals.insert(l, newInterval)

        # merge pass
        res = []
        for interval in intervals:
            # if res stack empty or most recently added interval in stack 
            # has an end time less than the current one's start time
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # there's an overlap, so merge the interval with the most recent one
            # by updating the most recent one's end time to whatever is bigger between
            # the most recent one and the current interval
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res