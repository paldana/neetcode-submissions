class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ## Greedy - Sort by End
        # Time: O(n log(n))
        # Space: O(n)
        intervals.sort(key = lambda pair: pair[1]) # T: O(n log(n)), S: O(n)
        prevEnd = intervals[0][1]
        overlaps = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                overlaps += 1
            else:
                prevEnd = intervals[i][1]   # we keep the intervals that ends early to leave more room for future intervals and reducing chance of overlap later


        return overlaps