class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointer solution
        i = j = 0       # initialize pointers for each string inputs

        # go through the string
        while i < len(s) and j < len(t):
            # if there's a match, move the pointer for s
            if s[i] == t[j]:
                i += 1
            j += 1          # keep incrementing the pointer for t whether if there's a match or not
                            # since we want to see if there's a subsequence or chars in the t string
        
        return i == len(s)  # if by the end of the loop, the len(s) matches the i pointer, then True 
                            
