class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## Brute Force - Recursion - first personal attempt - time limit exceeded at test 85/88 - not bad :D
        # Time: O(2^n)
        # Space: O(n)
        # def dfs(steps, amount):
        #     if steps >= len(cost):
        #         return amount
        #     amount += cost[steps]
        #     return min(dfs(steps + 1, amount), dfs(steps + 2, amount))
        # return min(dfs(0, 0), dfs(1, 0))

        ## Recursion - NC solution - same issue when submitting, exceeding time limit at test 85/88 - meaning my answer above also works :D
        # Time: O(2^n)
        # Space: O(n)
        # def dfs(steps):
        #     if steps >= len(cost):
        #         return 0
        #     return cost[steps] + min(dfs(steps + 1), dfs(steps + 2))
        # return min(dfs(0), dfs(1))

        ## DP - Memoization Approach (Top Down)
        # Time: O(n)
        # Space: O(n)
        # def dfs(steps, cache):
        #     if steps >= len(cost):
        #         return 0
        #     if steps in cache:
        #         return cache[steps]
        #     cache[steps] = cost[steps] + min(dfs(steps + 1, cache), dfs(steps + 2, cache))
        #     return cache[steps]

        # return min(dfs(0, {}), dfs(1, {}))

        ## DP (Bottom Up)
        # Time: O(n)
        # Space: O(n)
        n = len(cost)
        dp = [0] * (n + 1)      # dp[i] represent the minimum cost to reach step i.

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]
