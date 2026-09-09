from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magCounter = Counter(magazine)

        for ch in ransomCounter:
            if ch not in magCounter or ransomCounter[ch] > magCounter[ch]:
                return False
            
        return True