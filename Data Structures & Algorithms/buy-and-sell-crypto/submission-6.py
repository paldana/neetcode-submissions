class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        prevPrice = 0

        for price in prices:
            if minBuy < price:
                maxP = max(maxP, price - minBuy)
            
            minBuy = min(minBuy, price)
        return maxP

# One Pass array
# Time: O(n), Space: O(1)