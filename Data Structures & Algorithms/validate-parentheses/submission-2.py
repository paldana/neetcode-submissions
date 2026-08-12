class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {'}': '{', ']': '[', ')':'('}
        stack = []

        for par in s:
            if par in parMap:
                if stack and stack[-1] == parMap[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        
        return False if stack else True