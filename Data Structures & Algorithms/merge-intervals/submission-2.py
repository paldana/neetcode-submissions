class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sweep Line Algorithm
        # Time: O(n * log(n)), Space: O(n), where n is number of intervals in the list
        
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        """ i.e. intervals = [[1,3],[1,5],[6,7]]
            mp[1] = 2   - there are 2 intervals starting at 1
            mp[3] = -1
            mp[5] = -1      
            mp[6] = 1
            mp[7] = -1

            as we go through the for-loop below, we'll only add the interval to the res list
            once we have no active intervals (have == 0), effectively merging the two intervals
        """

        res = []
        interval = []
        have = 0                        # number of active intervals
        for i in sorted(mp):
            if not interval:
                interval.append(i)      # append start time to interval if empty to start new interval pair
            have += mp[i]               
            if have == 0:               # once we see an interval just ended, we get the value of the current i as it will be the end time for the interval
                interval.append(i)      # append the end time to the current active interval pair
                res.append(interval)
                interval = []           # reset interval to get the new start time of the subsequent interval to be appended to res
        return res