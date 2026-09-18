## Dynamic Programming - Bottom-Up Approach
# Time and Space: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}    # initialize dp map with 1 element in the event that we're given an empty string, we can still return "1"

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]   # if digit i is 1-9 -- single digit value

            ## 2-digit value
            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]