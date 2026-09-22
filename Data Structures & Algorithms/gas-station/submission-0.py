class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # edge case - confirm that we have more than enough gas to traverse the circuit
        if sum(gas) < sum(cost):
            return -1       # not possible to complete otherwise
        
        fuel = 0
        startIdx = 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]

            # if fuel becomes negative, current index is not a possible answer since we won't 
            # be able to move to the next station, so we'd reset the fueul to 0 and update the 
            # start index to the next iteration
            if fuel < 0:
                fuel = 0
                startIdx = i + 1
        

        # after the for-loop, whatever the startIdx is would be the correct answer since we were 
        # guaranteed that there's only ONE solution. Although we technically didn't go "around"
        # the gas station circuits, we know that any of the indices before we got to where the startIdx is
        # wouldn't be a valid solution AND since we know that there are more than enough gas
        # to complete the circuit (checked from the edge case above), we can safely assume that
        # we can finish the whole circuit after going through the list once.

        return startIdx

        