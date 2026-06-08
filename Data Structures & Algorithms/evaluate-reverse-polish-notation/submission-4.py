class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for tkn in tokens:
            # check every element of tokens and perform the op if an operator sign is seen
            if tkn in ops:
                # pop 2 numbers from stack and perform operation
                newVal = 0
                match tkn:
                    case '+':
                        op1, op2 = stack.pop(), stack.pop()
                        newVal = op2 + op1
                    case '-':
                        op1, op2 = stack.pop(), stack.pop()
                        newVal = op2 - op1
                    case '*':
                        op1, op2 = stack.pop(), stack.pop()
                        newVal = op2 * op1
                    case '/':
                        op1, op2 = stack.pop(), stack.pop()
                        newVal = int(op2 / op1)  # int truncates the decimal part (rounds toward zero)
                stack.append(newVal)
            else:
                stack.append(int(tkn))
        
        return stack[0]

# Stack Method
# Time and Space Complexity: O(n)