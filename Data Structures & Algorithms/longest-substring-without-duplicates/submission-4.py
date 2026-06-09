class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointer - Sliding Window Solution
        # Time: O(n), Space: O(m); 
        # where n = length of s, m = total of unique char in string
        l = 0
        maxL = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxL = max(maxL, (r - l)+ 1)
        
        return maxL