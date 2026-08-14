class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        
        s1Freq, s2Freq = {}, {}
        # map all characters in s1
        for i in range(n1):
            s1Freq[s1[i]] = s1Freq.get(s1[i], 0) + 1
        
        # sliding window method to go through the s2 characters
        l = 0
        for r in range(n2):
            # check if current window (r-l+1) is bigger than size of s1, shrink sliding window
            while (r - l + 1) > n1:
                s2Freq[s2[l]] -= 1
                if s2Freq[s2[l]] == 0:
                    del s2Freq[s2[l]]    # delete the key from the map as we'll be comparing the maps
                l += 1
            
            s2Freq[s2[r]] = s2Freq.get(s2[r], 0) + 1
            if s1Freq == s2Freq:
                return True
        
        return False

# Sliding Window x Hashmap solution
# Time complexity: O(n)
# Space complexity: O(1)

