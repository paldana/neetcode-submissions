class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCharMap = [0] * 26

        for ch in magazine:
            magCharMap[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            magCharMap[ord(ch) - ord('a')] -= 1
            if magCharMap[ord(ch) - ord('a')] < 0:
                return False
        
        return True

# Array Manipulation Approach
# Time Complexity: O(n + m), n and m = number of chars within ransomNote and magazine, respectively
# Space Complexity: O(26) --> O(1) constant space
