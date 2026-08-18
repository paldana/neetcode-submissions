class Solution:
    def climbStairs(self, n: int) -> int:
        ## Dynamic Programming - Bottom-up Solution
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        print(f"{dp=}")
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]