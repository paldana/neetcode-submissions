class Solution:
    def climbStairs(self, n: int) -> int:
        ## Brute Force - Recursion
        # Time: O(2^n) - due to the 2 DFS recursions
        # Space: O(n) ? -- or O(1)?

        # def dfs(steps):
        #     if steps >= n:
        #         return steps == n
        #     return dfs(steps + 1) + dfs(steps + 2)    
        # return(dfs(0))

        ## Dynamic Programming - Bottom-up
        if n <= 2:
            return n
        
        dp = [0] * (n+1)    # create an array which will contain the number of steps that will be needed to get to ith-step
                            # n+1 because 0-indexed
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]   # steps it needs to take to get to ith step is the sum of the steps it needs to make it to the previous 2 steps
                                        # similar to fibonacci

        return dp[i]


