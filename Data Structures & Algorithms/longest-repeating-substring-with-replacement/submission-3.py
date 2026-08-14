class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Need to determine the longest string possible after replacing k chars 
        freqMap = {}    # key: char; val: num of occurence
        maxLength, maxFreq = 0, 0
        l = 0

        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1  # increment occurence of current char in the map
            maxFreq = max(maxFreq, freqMap[s[r]])     # update maxFreq to get the num of most occuring char
            
            # currentWindow = (r - l) + 1   # +1 since 0-indexed; using this variable won't recalculate values as l updates below
            # currentWindow - maxFreq = num of replaceable chars 
            # determine the longest possible string after replacing k chars    
            while (r - l + 1) - maxFreq > k:      
                # while not num of replaceable chars <= k, we shorten the currentWindow
                freqMap[s[l]] -= 1  # reduce the num of occurence of char s[l]
                l += 1              # move the l pointer

            maxLength = max(maxLength, (r - l) + 1)
        
        return maxLength
                
# Optimal Sliding Window
# time: O(n); space: O(m)
# where n is the length of the string and 
# m is the total number of unique characters in the string.


        
        