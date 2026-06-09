class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = eating rate; min. speed will be 1 and max. speed is max(piles)
        kL, kR = 1, max(piles)
        minK = max(piles)
        while kL <= kR:
            totalTime = 0
            kM = kL + (kR - kL)//2
            
            for pile in piles:
                totalTime += math.ceil(pile/kM)
            
            if totalTime <= h:
                minK = min(minK, kM)
                kR = kM - 1
            else:
                kL = kM + 1
        
        return minK