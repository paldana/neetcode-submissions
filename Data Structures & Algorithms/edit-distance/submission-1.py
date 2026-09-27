## Dynamic Programming - Top-Down : Memoization x Recurssion
# Time and Space: O(3^(m+n))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}

        # i, j pointer for word1 and word2, respectively
        def dfs(i, j):
            if i == m:          # reached end of word1
                return n - j        # return rest of word2
            if j == n:          # reached end of word2
                return m - i        # return rest of word1
            
            if word1[i] == word2[j]:    # chars from both words matches
                return dfs(i + 1, j + 1)    # move both pointers to next position
            if (i,j) in memo:
                return memo[(i,j)]

            ## take minimum operations from these 3 ops:
                # delete from word1: dfs(i + 1, j)
                # insert into word1: dfs(i, j + 1)
                # replace the character: dfs(i+1, j+1)
            res = min(dfs(i + 1, j), dfs(i, j + 1))
            res = min(res, dfs(i + 1, j + 1))
            memo[(i,j)] = res + 1
            return memo[(i,j)]      # +1 for current operation

        return dfs(0, 0)