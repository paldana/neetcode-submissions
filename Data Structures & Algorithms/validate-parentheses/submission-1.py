class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'}': '{', ')': '(', ']': '['}
        stack = []
        for par in s:
            if par in hashmap:
                if stack and hashmap[par] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        
        return False if stack else True

# Stack method
# Time: O(n); Space: O(n)