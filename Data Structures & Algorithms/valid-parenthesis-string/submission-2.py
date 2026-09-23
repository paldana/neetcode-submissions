## Greedy Approach
# Time: O(n), Space: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftMin/leftMax - min/max possible number of unmatched '('
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:   # c == "*" - can be '(', ')', or empty string
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            if leftMax < 0:     # if there are more ) than ( or * combined
                return False
            if leftMin < 0:     # leftMin can be negative since there can be multiple * be added, but will not affect the validity of the string
                leftMin = 0
        return leftMin == 0