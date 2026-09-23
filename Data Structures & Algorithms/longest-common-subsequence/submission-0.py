## 2D Dynamic Programming - Bottom - Up
# Time: O(n * m)
# Space: O(n * m) - dp grid
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # create a 2D DP grid where m will be used as number of rows, and n for number of cols
        # The values of the dp grid will contain the number of subsequence
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        # +1 are for the dp's border, which will be 0s by design. 
        

        # start from the bottom right of the matrix
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:                # once we get a match, 
                    dp[i][j] = 1 + dp[i + 1][j + 1]     # get the diagonal count for the number of subsequence, +1 for the current match
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i+1][j])    # get the max val of the subsequence between the right and bottom cells
                                                       # this is done for us to be able to get the number of common subsequence from the
                                                       # prior rows/cols. If not done, we won't be able to get the correct number of subsequence
        
        return dp[0][0]     # at the end of the for loop, this will contain the LCS number


# Note: This solution would be easier to explain when drawn out to make sense of the for-loop else statement