class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}    # key: char, value: last index where char was seen
        maxL, l = 0, 0

        for r in range(len(s)):
            if s[r] in charMap:
                l = max(charMap[s[r]] + 1, l)       ## Revisit this
            charMap[s[r]] = r
            maxL = max(maxL, (r-l)+1)
        return maxL