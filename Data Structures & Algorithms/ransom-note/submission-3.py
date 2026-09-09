class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charCount = [0] * 26        # will contain count of every letter in the alphabet

        # extract all available letters from magazine
        for c in magazine:
            charCount[ord(c) - ord('a')] += 1
        
        # check if we'll be able to construct ransomNote from the available number of letters we got from magazine
        for c in ransomNote:
            charCount[ord(c) - ord('a')] -= 1
            # check if we still have valid amount of letters left in the array
            if charCount[ord(c) - ord('a')] < 0:    
                return False        # returns False if we exceed the amount of letters available in the magazine
        
        return True

    ## Count Frequency - Space Optimized 
    # Time Complexity: O(r+m)
    # Space Complexity: O(1) since we have at most 26 different characters
    # -- where r and m are number of chars in ransomNote and magazine, respectively 