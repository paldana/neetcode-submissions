class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window x Hash Map Solution (optimal)
        # Time: O(n), Space: O(m); 
        # where n = length of s, m = total of unique char in string
        map = {}  # key: char, value: last index where character appeared
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in map:             # if a duplicate is found
                # prevent the l pointer from moving backwards if the last occurence of the
                # duplicate character happened before the current window (l -> r) start
                l = max(map[s[r]] + 1, l)   
            map[s[r]] = r               # update the last occurence of the char
            res = max(res, r - l + 1)   # update the longest substring length
        return res
