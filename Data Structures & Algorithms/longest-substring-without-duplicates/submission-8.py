class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ### Sliding Window Solution ###
        ## Hashmap method ##
        charMap = {}        # key: char; value: last index where character was seen
        maxL, l = 0, 0

        for r in range(len(s)):
            # go through each char of s and see if they're already added to the hashmap
            if s[r] in charMap:
                # update the l pointer to point to the index right next to where s[r] is last seen
                l = max(l, charMap[s[r]] + 1)    # this is done to prevent l pointer from moving backwards 
                                        # in the event that the last occurence index was before the 
                                        # start of the current contiguous sequence window (l -> r)

            # update the index of the character in s[r] 
            charMap[s[r]] = r
            
            # calculate the length of the sequence window 
            maxL = max(maxL, (r - l) + 1)       # +1 since 0-indexed
        
        return maxL

# Time Complexity: O(n)
# Space Complexity: O(m)
# where n = length of s, m = total of unique char in string
            
