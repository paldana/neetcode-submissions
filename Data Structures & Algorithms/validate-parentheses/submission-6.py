class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:     # if length of s is odd, return false
            return False
        
        openSet = ('[', '(', '{')
        closeSet = (']', ')', '}')
        hashmap = {'[': ']', '(': ')', '{': '}'}        # key: opening par, value: closing par
        stack = []

        for p in s:
            if p in openSet:
                stack.append(p)
            elif p in closeSet:
                if stack and hashmap[stack[-1]] == p:
                    stack.pop()
                else:
                    return False
            else:
                # if we received chars other than the parenthesis expected
                return False
        
        return len(stack) == 0
        