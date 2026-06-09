class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers - Sliding window -> time: O(n^2); space: O(1)
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            # if we see a drop in price the next day, we move the l pointer to where r is
            if prices[r] < prices[l]:
                l = r
            else:   # we see price increase, we keep moving the r pointer
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
        
        return maxProfit

            