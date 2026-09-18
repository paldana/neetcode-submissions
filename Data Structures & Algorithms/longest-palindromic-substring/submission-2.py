## Dynamic Programming Approach 
# Time Complexity: O(n^2)
# Space: O(n^2) 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)
        # create a dp matrix that will store if a particular i,j pointer pair has been checked and confirmed a palindrome
        dp = [[False] * n for _ in range(n)]    

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # j - i <= 2 --> special small case if length is 1,2,or 3, then matching end is enough because mid char doesn't matter
                # dp[i + 1][j - 1]) --> check if inner chars are palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):        # update max length and starting index of the substring
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]