## Dynamic Programming - Top-Down - Memoization x Recursion
# Time: O(2 * n) - one each for buying/selling and cooldown -> O(n)
# Space


"""
    3 State: Buying or Selling or Cooldown/Do Nothing
    buying: i + 1, then deduct purchase price[i]
    selling: i + 2, then add profit/loss price[i]
        --> +1 for the cooldown day after selling
    cooldown: i + 1, either you already own a stock or just sold one
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}   # key: (i, buying), value: maxProfit
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in memo:
                return memo[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
                
            return memo[(i, buying)]
        
        return dfs(0, True)