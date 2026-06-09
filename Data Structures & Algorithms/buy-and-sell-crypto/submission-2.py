class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force - time: O(n^2); space: O(1)
        maxProfit = 0
        totalDays = len(prices)

        for i in range(totalDays):
            purchasePrice = prices[i]
            for j in range(i+1, totalDays):
                sellPrice = prices[j]
                maxProfit = max(maxProfit, sellPrice - purchasePrice)
        return maxProfit