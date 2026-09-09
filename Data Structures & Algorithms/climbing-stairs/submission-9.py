class Solution:
    def climbStairs(self, n: int) -> int:
        ## Brute Force - Recursion
        # Time: O(2^n) - due to the 2 DFS recursions
        # Space: O(n), where n is total number of elements procured from input n (total number of stairs)

        # def dfs(steps):
        #     if steps >= n:
        #         return steps == n
        #     return dfs(steps + 1) + dfs(steps + 2)    
        # return(dfs(0))

        ## Dynamic Programming - Top-Bottom - memoization using Hash map
        # Time and Space: O(n)
        # def dfs(steps, cache):
        #     if steps >= n:
        #         return steps == n
        #     if steps in cache:
        #         return cache[steps]
        #     cache[steps] = dfs(steps + 1, cache) + dfs(steps + 2, cache)
        #     return cache[steps]
        # return dfs(0,{})
        

        ## Dynamic Programming - Bottom-up
        # Time and Space: O(n)
        # if n <= 2:
        #     return n
        # dp = [0] * (n+1)    # create an array which will contain the number of steps that will be needed to get to ith-step
        #                     # n+1 because 0-indexed
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]   # steps it needs to take to get to ith step is the sum of the steps it needs to make it to the previous 2 steps
        #                                 # similar to fibonacci
        # return dp[i]

        ## Dynamic Programming - Bottom-up - Hashmap version
        # Time and Space: O(n)
        # if n <= 2:
        #     return n
        # dp = {}             # create a dict which will contain the number of steps that will be needed to get to ith-step
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]   # steps it needs to take to get to ith step is the sum of the steps it needs to make it to the previous 2 steps
        #                                 # similar to fibonacci
        # return dp[i]


        ## Dynamic Programming (Space Optimized) -- good luck explaining during interview 
        Time: O(n)
        Space: O(1)
        one, two = 1, 1
        for _ in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

