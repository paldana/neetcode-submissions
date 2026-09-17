class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # given an intervals list [start_i, end_i], sorted by start_i
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
            # if new interval ends first before the first interval in the list even start, 
            # simply insert it as the first interval in the list
                res.append(newInterval)     
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
            # if new interval starts after the current interval's start, add the current interval
            # to the list first - no merge yet
                res.append(intervals[i])
            else:
            # there's an overlap, so we'd need to merge the current interval with the new one 
            # and update the new interval as the expanded one to be compared to subsequent intervals remaining
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # we don't want to put it to the res yet until we're sure there's no need to merge intervals
        
        res.append(newInterval)
        return res

## Greedy Approach
# Time: O(n), Space: O(n)