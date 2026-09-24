## Practice
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}   # key: (i, buying/selling), value: maxProfit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
            
            return memo[(i, buying)]
        
        return dfs(0, True)