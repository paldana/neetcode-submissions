class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add an open parentheses if open < n
        # only add a close parentheses if close < open
        # Valid set IIF close == open == n
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

            return
        
        backtrack(0, 0)
        return res