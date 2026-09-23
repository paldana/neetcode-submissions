## Greedy Solution
"""
    1. create a map for the letters in the string s that will store the last index when they appeared
    2. Maintaining 2 variables: partition "size" and "end" 
       - Go through the string again and save the last index of every character we iterate through until
         we get to that index. Once we get to that index, save the partition size and reset to get the next one. 
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1.
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        # 2.
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])    # update end if the current character has a farther index
            
            # save partition size once we get to the end index
            # this means that we've reached an end of a partition where each letter appears 
            # in at most one substring
            if i == end:                   
                res.append(size)
                size = 0
        
        return res
