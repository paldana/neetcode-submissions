## Backtracking Approach - Simplest Solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
                return

            for j in range(i, len(s)):
                w = s[i:j + 1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j + 1)
                    cur.pop()

        cur = []
        res = []
        backtrack(0)
        return res        

"""
Time & Space Complexity
Time complexity: O(m + n * 2^n)
Space complexity: O(m + 2^n)
 
Where 
n is the length of the string s and m
m is the sum of the lengths of the strings in the wordDict.

"""