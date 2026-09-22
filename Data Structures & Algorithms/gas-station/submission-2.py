## Two Pointer Solution
# Time: O(n), Space: O(1), where n is the length of gas and cost arrays
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, end = n - 1, 0           # start at the end of the list, end at the beginning 
        tank = gas[start] - cost[start]
        while start > end:
            if tank < 0:                            # if tank is negative, move start backward to find more gas
                start -= 1
                tank += gas[start] - cost[start]
            else:                                   # if there's enough gas from the start, extend the route
                tank += gas[end] - cost[end]        
                end += 1
        return start if tank >= 0 else -1           # once start and end meet, check if we made it without tank going negative