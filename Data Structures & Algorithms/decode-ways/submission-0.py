## Dynamic Programming - Top-Down Approach + recursion
# Time and Space: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)      # recursion for a single digit value
            # first check if we can check a 2nd digit before actually checking it
            if i + 1 < len(s) and (
                s[i] == "1" or                          # first digit is 1 - 2nd digit can be from "0-9"
                s[i] == "2" and s[i + 1] in "0123456"   # first digit is 2 - 2nd digit can be from "0-6"
            ):
                res += dfs(i + 2)   # do another recursion for a double digit value, if possible
            dp[i] = res             # cache the result
            return res

        return dfs(0)