class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {'}':'{', ')': '(', ']': '['}
        stack = []

        for par in s:
            if par in parMap:
                if stack and parMap[par] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        
        return len(stack) == 0