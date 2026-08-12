class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        # put the position and speed values of respective cars in a single list, pairs
        pairs = [(p, s) for p, s in zip(position, speed)]
        # sort the pairs list to have the position closest to the target first
        pairs.sort(reverse=True)

        ### Stack Method ###
        # create a list of each fleet's ETAs (lower value = faster)
        # eta = []
        # for pos, spd in pairs:
        #     eta.append((target - pos)/spd)

        #     # check if the top 2 fleet in the eta stack has the potential to merge
        #     # eta[-2] = previous fleet, closer to the target position, eta[-1] = most recent fleet added
        #     # if eta[-2] is slower (longer ETA) than eta[-1], the two fleet will merge (by popping the stack)
        #     # since the faster fleet cannot overtake; 
        #     if len(eta) >= 2 and (eta[-2] >= eta[-1]):
        #         eta.pop()
        
        # return len(eta)

        # time complexity: O(n log n) - n for going through the list; log n for sorting
        # space complexity: O(n)

        ### Iteration Method ###
        # calculate the ETA of the first pair and initialize the fleets count to 1
        fleets = 1
        prevEta = (target - pairs[0][0]) / pairs[0][1]

        # go through the rest of the car pairs and calculate their ETAs
        for i in range(1, len(pairs)):
            pos, spd = pairs[i]
            currEta = (target - pos) / spd

            # if previous ETA is faster (less) than the currently calculated ETA, inc fleet as they will not merge
            # and update the prevEta to currEta to see if the subsequent ETAs will merge
            if prevEta < currEta:
                fleets += 1
                prevEta = currEta
                
        return fleets

        # Time: O(n log n) 
        # Space: O(n)

