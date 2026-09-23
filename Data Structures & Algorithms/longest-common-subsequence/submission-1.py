## Dynamic Programming Top-Down Approach - Memoization x Recursion 
# Time: O(2^(m+n))
# Space: O(m + n)
# where m and n are lengths of text1 and text2, respectively
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}   # key: indices (i, j), value: LCS at cell(i,j)

        # find the LCS at cell (i,j)
        def dfs(i, j):
            # base case - if we've reached the end of either string
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            # if current char matches
            if text1[i] == text2[j]:
                # add 1 for LCS and recurse to the next char for both strings
                memo[(i,j)] = 1 + dfs(i + 1, j + 1)
            else:
                # recurse by skipping text1[i] or text2[j] and return the maximum
                memo[(i,j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i,j)]

        return dfs(0, 0)
