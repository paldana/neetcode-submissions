## Greedy Solution Practice
# Time: O(n) - we go through the whole string s once
# Space: O(1) - no extra space
class Solution:
    def checkValidString(self, s: str) -> bool:
        # min/max number of "("
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:   # * - can be (, ), or an empty string
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            # if at any point leftMax becomes negative, it means we have too many )
            if leftMax < 0:
                return False
            
            # on the other hand, having a negative leftMin is OK since we may have a lot of * in the string.
            # if that happens, reset the leftMin to 0 to be used to return the result
            if leftMin < 0:
                leftMin = 0
        
        # if at the end of the iteration, leftMin > 0 - that means that there's an unclosed ( remaining, hence not a valid string
        return leftMin == 0