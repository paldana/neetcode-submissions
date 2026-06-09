class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        res = 0
        l = 0

        for r in range(len(s)):

            map[s[r]] = map.get(s[r], 0) + 1

            while (r-l+1) - max(map.values()) > k:
                map[s[l]] -= 1
                l += 1

            res = max(res, r-l + 1)
        return res

# Sliding Window
# time: O(m * n); space: O(m)
# where n is the length of the string and 
# m is the total number of unique characters in the string.