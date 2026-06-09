class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            map[s[r]] = map.get(s[r], 0) + 1
            maxf = max(maxf, map[s[r]])
            while (r - l + 1) - maxf > k:
                map[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

# Optimal Sliding Window
# time: O(n); space: O(m)
# where n is the length of the string and 
# m is the total number of unique characters in the string.