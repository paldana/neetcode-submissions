class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounter, tCounter = {}, {}

        for i in range(len(s)):
            sCounter[s[i]] = sCounter.get(s[i], 0) + 1
            tCounter[t[i]] = tCounter.get(t[i], 0) + 1
            
        return sCounter == tCounter