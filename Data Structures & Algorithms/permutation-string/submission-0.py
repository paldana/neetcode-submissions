class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            # in the event that increasing the char at index count by 1,
            # there'll be a mismatch, so decrease the matches count
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # since we're moving the window, check the left char index
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1     # decreasing accordingly as we move the sliding window
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1
        
        return matches == 26


## Sliding window solution - using Array instead of Hashmaps
# Time complexity: O(n)
# Space complexity: O(1)
# pretty confusing algorithm, tbh -- look for a better algo

