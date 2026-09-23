## Stack Approach
# Time and Space: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        open = []
        star = []   # can be treated as (, ), or an empty string

        for i, ch in enumerate(s):
            if ch == '(':
                open.append(i)
            elif ch == '*':
                star.append(i)
            else:  # ch == ')'
                # if there's an imbalance of )
                if not open and not star:
                    return False
                if open:
                    open.pop()
                else:
                    star.pop()
        
        # after going through the string, check if there are more
        # open bracket than the remaining star. If there are, then invalid.
        while open and star:
            if open.pop() > star.pop():
                return False
        return not open