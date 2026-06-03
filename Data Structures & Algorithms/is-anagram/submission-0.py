class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if length of both string inputs are the same
        if len(s) != len(t):
            return False
        
        # using dict/hash map to store the count (as value) of each char (as index)
        sCounter, tCounter = {}, {}

        for i in range(len(s)):
            # increment the char count of each character found in the inputs
            sCounter[s[i]] = sCounter.get(s[i], 0) + 1 
            tCounter[t[i]] = tCounter.get(t[i], 0) + 1 
        
        # returns True if all char counts are equal == Anagram
        return (sCounter == tCounter)

# Time: O(n)
# Size: 