class Solution:
    ## Dynamic Programming Approach - Bottom Up
    # Time Complexity: O(n * t)
    # Space Complexity: O(n)
    # - where n = len(coins), t = given amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)    # create an array that will initially store a max number (in this case, amount + 1)
                                            # this will store the min. amount of coins needed
        dp[0] = 0                           # base case - 0 coins for 0 amount

        # compute every amount in the dp array - starting from 1 (bottom-up)
        for a in range(1, amount + 1):
            for c in coins:                 # for every coin in the coins list
                if a - c >= 0:              # if non-negative
                    dp[a] = min(dp[a], 1 + dp[a - c])       # note: the 1 in 1 + dp[a-c] is accounting for the current coin, c
                    
                    # ex. a = 7, c = 4 -> dp[7] = min(dp[7], 1 + dp[3]) -- dp[3] has been computed in prior iterations and 
                    #                                                      dp[7] is not yet updated, so it still has amount + 1 as its value


        return dp[amount] if dp[amount] != amount + 1 else -1       # make sure to check if the value in dp has been updated and not the max value we initially set it to
