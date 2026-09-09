class Solution:
    ## Pure DFS Approach 
    # Time: O(n^t)
    # Space: O(t)
    # - where n = len(coins), t = amount
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # dfs will return the min number of coins we can get to amt
    #     def dfs(amt):
    #         if amt == 0:
    #             return 0
    #         res = amount + 1  # can be just an arbitrary large number
    #         for coin in coins:
    #             if amt - coin >= 0:
    #                 res = min(res, 1 + dfs(amt - coin))
    #         return res
        
    #     minCoins = dfs(amount)
    #     return minCoins if minCoins != amount + 1 else -1


    ## Dynamic Programming - DFS x Memoization
    # Time: O(n*t)
    # Space: O(t)
    # - where n = len(coins), t = amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        # dfs will return the min number of coins we can get to amt
        def dfs(amt):
            if amt == 0:
                return 0

            if amt in cache:
                return cache[amt]

            res = amount + 1  # can be just an arbitrary large number
            for coin in coins:
                if amt - coin >= 0:
                    res = min(res, 1 + dfs(amt - coin))

            cache[amt] = res
            return res
        
        minCoins = dfs(amount)
        return minCoins if minCoins != amount + 1 else -1