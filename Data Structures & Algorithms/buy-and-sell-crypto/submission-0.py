class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force - time: O(n^2); space: O(1)
        minPrice = 0
        maxProfit = 0
        
        totalDays = len(prices)

        for i in range(totalDays):
            currPrice = prices[i]
            for j in range(i, totalDays):
                maxProfit = max(maxProfit, prices[j] - currPrice)
        
        return maxProfit