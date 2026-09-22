## Dynamic Programming - Top-Down Approach (Memoization of Brute Force)
# Time: O(n * m * t), Space: O(n)
# Where n is the length of the string s, 
#       m is the number of words in wordDict and 
#       t is the maximum length of any word in wordDict.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}       # key: index, value: if we've already visited it, it will show a boolean reuslt if a word matches at that index - caching

        def dfs(idx):
            if idx in memo:
                return memo[idx]
            
            for word in wordDict:
                wordLen = len(word)
                if idx + wordLen <= len(s) and s[idx : idx + wordLen] == word:
                    if dfs(idx + wordLen):
                        memo[idx] = True
                        return True
                 
            memo[idx] = False
            return False

        return dfs(0)