class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {'[': ']', '(': ')', '{': '}'}        # key: opening par, value: closing par
        stack = []

        for par in s:
            if par in parMap:
                stack.append(par)
            else:
                if stack and parMap[stack[-1]] == par:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0 