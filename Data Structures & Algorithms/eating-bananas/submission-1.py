class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = eating rate; min. speed will be 1 and max. speed is max(piles)
        kL, kR = 1, max(piles)
        minK = max(piles)

        while kL <= kR:
            totalTime = 0                       
            kM = kL + (kR - kL)//2          # get the 'mid' of the speed rate

            for pile in piles:              # iterate through the piles list to get the total time 
                totalTime += math.ceil(pile/kM)     # to consume all in the current rate, kM
            
            if totalTime <= h:              # if totalTime is within alotted time, 
                minK = min(minK, kM)        # update minK and keep looking for smaller K
                kR = kM - 1
            else:
                kL = kM + 1
        
        return minK

    # Binary Search
    # Time Complexity: O(n * log m); 
    #   where is the number of piles, and m is the max. number of bananas in the pile
    # Space Complexity: O(1)