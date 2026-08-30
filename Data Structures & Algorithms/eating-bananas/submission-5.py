class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## 2 pointer solution - find the min rate K to finish all bananas within h hours
        # range for l and r pointers: banana eating rate
        # limit would be the max number of bananas in a single pile in the piles list
        kL, kR = 1, max(piles)
        kMin = kR

        # piles.sort()

        while kL <= kR:
            kMid = (kL + kR) // 2
            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(pile/kMid)
            
            if totalTime <= h:      # kMid is within alotted time, so we can go slower
                kR = kMid - 1       # reduce the kR to continue finding the minK
                kMin = min(kMin, kMid)
            elif totalTime > h:
                kL = kMid + 1
            
        return kMin
            

