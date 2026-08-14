class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxL, l = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            maxL = max(maxL, (r - l) + 1)   # 0-indexed so +1

        return maxL