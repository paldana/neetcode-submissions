## 2-pointer Approach - simplest and better than BS Dynamic Programming solution
# Time Complexity: O(n^2)
# Space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)      # for odd number length substrings
            res += self.countPali(s, i, i + 1)  # for even number
        return res

    ## count palindrome substrings starting from the middle char, expanding left and right
    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:   # check if we're in allowed range and if palindrome
            res += 1
            l -= 1
            r += 1
        return res