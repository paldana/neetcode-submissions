## Dynamic Programming - Top-Down - Memo x Recursion
# Time and Space: O(n * m), where n and m are lengths of s and t, respectively
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}   # key: (i,j), value: num of distinct sequence at i,j

        def dfs(i, j):
            # if we've reached end of t, we've found a distinct subsequence
            if j == len(t):
                return 1
            # if we've reached end of s and not yet of t, then it's not possible to get a subsequence from this i,j - return 0
            if i == len(s):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == t[j]:
                # recurse 2 possible ways, 1st by moving both index to the next position and 2nd by just moving i to look for matching values that can possibly lead to another distinct subsequence
                memo[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # if not a match, move i to find for a match with t
                memo[(i,j)] = dfs(i + 1, j)
            
            return memo[(i,j)]
        
        return dfs(0, 0)
                