from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## Binary Search Solution ##
        kL, kR = 1, max(piles)
        minK = max(piles)

        # goal is to get the min rate, minK, possible to finish all bananas by hour, h
        while kL <= kR:
            kMid = (kL + kR) // 2
            totalTime = 0
            for pile in piles:
                totalTime += ceil(pile/kMid)
            
            # if total time is within alotted time h, update minK to get the min value and keep iterating until done with loop
            if totalTime <= h:   
                minK = min(minK, kMid)
                kR = kMid - 1   # rate can be less than the current kMid to make the answer closer to min. K
            else: # totalTime > h:
                kL = kMid + 1
                
        return minK
            
            



