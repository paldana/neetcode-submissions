class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        l, r = 0, 1
        maxProfit = 0
        lowestPrice = prices[0]
        while r < len(prices):
            # if we see a drop in price the next day, we move the l pointer to where r is
            if prices[r] < prices[l] and prices[r] < lowestPrice:
                lowestPrice = prices[r]
                l = r
            else:   # we see price increase, we keep moving the r pointer
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
        
        return maxProfit

            