from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## find the minimum rate possible to eat all the bananas from the piles
        # since we're looking for the RATE and not the number of bananas, 
        # we'll have to go through possible rates in the algo. 
        # To do this, we'll have to establish the boundaries for the rate.
        # Given the constraint: h >= len(piles), we can assume that the upper rate boundary,
        # kR, to be the max number of banana in a single pile in piles,
        # as we're guaranteed that we can always finish by h. We can have the lower rate 
        # boundary, kL, to be 1.
        kL, kR = 1, max(piles)
        kMin = max(piles)   # we can start with the min rate to be the max num of bananas in a pile

        # perform binary search to determine the minK
        while kL <= kR:
            kMid = (kL + kR) // 2
            totalTime = 0

            for pile in piles:
                # use math.ceil in order to determine how much time it'll take for Koko to eat a pile of banana per rate kMid
                totalTime += ceil(pile/kMid)

            
            if totalTime <= h:
                # time is within the h window, so we know that the rate is acceptable, but we'll need the min rate possible
                kMin = min(kMin, kMid)
                kR = kMid - 1       # keep going through the loop and move the upper boundary to the left of mid
            else:   # totalTime > h
                kL = kMid + 1       # we'll need a higher rate to be within the h window, so increase the lower rate boundary
            
        # return the kMin possible after going through the loop
        return kMin

# Binary Search
# Time Complexity: O(n * log m); 
#   where n is the number of piles, and m is the max. number of bananas in the pile
# Space Complexity: O(1)



