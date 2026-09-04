class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        """ 
        We'll want to recurse in order to create a valid parentheses combination
        To do so, we'll have to keep track of the number of open and close parentheses 
        that we currently have. We know that a parentheses to be valid, it has to have an
        opening before a closing one. 
        
        Need to satisfy these conditions
        1. num of open par == num of closed par == n -> valid combination
        2. num of open par > num of closed par and n -> can still add an opening par
        3. num of open par > num of closed par -> can add a closing par
        
        """
        def backtrack(openN, closedN, currStack):
            if openN == closedN == n:
                res.append("".join(currStack))
                return
            
            if openN < n:
                currStack.append('(')
                backtrack(openN + 1, closedN, currStack)
                currStack.pop()
            
            if closedN < openN:
                currStack.append(')')
                backtrack(openN, closedN + 1, currStack)
                currStack.pop()
            
        backtrack(0, 0, [])

        return res
            