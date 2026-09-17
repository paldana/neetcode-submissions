class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ## Greedy - Sort by Start
        # Time: O(n log(n))
        # Space: O(n)
        intervals.sort()
        overlaps = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end       # update the prevEnd to the next interval's end to check overlaps with subsequent intervals
            else:
                overlaps += 1
                prevEnd = min(prevEnd, end) # keep the interval with the smaller end time
           
        return overlaps