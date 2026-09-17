class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)

        ## Merge interval pass
        res = []
        for interval in intervals:
            # append to res stack if it's empty or most recent interval end time is less than the current interval's start time
            if not res or res[-1][1] < interval[0]: 
                res.append(interval)
            else:   # else, there's an overlap, so update the most recent's end time with the higher end time between the most recent and the current intervals
                res[-1][1] = max(res[-1][1], interval[1])
        return res

## Binary Search Approach
# Time: O(n), Space: O(n)