## Dynamic Programming - Bottom-Up Approach
# Time: O(n * m * t), Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1 , -1):
            for w in wordDict:
                wordLen = len(w)
                # check if current word matches the substring in s
                if i + wordLen <= n and w == s[i:i+wordLen]:
                    dp[i] = dp[i + wordLen]     # this checks if the current substring completes a word; notice we started with the end of string as True to get this to work      
                    if dp[i]:
                        break
        
        return dp[0]
