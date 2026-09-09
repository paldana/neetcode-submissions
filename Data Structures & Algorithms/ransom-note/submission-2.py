# from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransomCounter = Counter(ransomNote)
        # magCounter = Counter(magazine)

        # alternatively, without using Counter
        ransomCounter, magCounter = {}, {}
        for c in ransomNote:
            ransomCounter[c] = ransomCounter.get(c, 0) + 1

        for c in magazine:
            magCounter[c] = magCounter.get(c, 0) + 1

        for ch in ransomCounter:
            if ch not in magCounter or ransomCounter[ch] > magCounter[ch]:
                return False

        return True


## Hashmap/Counter approach
# Time Complexity: O(r+m)
# Space Complexity: O(r+m)
