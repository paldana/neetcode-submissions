class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}

        l = 0

        for i in s1:
            freq1[i] = freq1.get(i, 0) + 1
        
        for r in range(len(s2)):
            while r - l + 1 > len(s1): # while invalid, shrink window
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0: 
                    del freq2[s2[l]]    
                l += 1  

            freq2[s2[r]] = freq2.get(s2[r], 0) + 1 # update answer when valid

            if freq1 == freq2:
                return True

        return False

## Someone's solution in the "Discuss" section
# Hashmap solution - 1
# Time complexity: O(n)
# Space complexity: O(1)