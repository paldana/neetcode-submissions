class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force - Time: O(n*m); Space: O(m)
        # where n = length of s, m = total of unique char in string
        maxLength = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])

            maxLength = max(maxLength, len(charSet))
        return maxLength