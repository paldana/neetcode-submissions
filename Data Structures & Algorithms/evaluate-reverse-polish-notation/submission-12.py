class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operands = ['+', '-', '/', '*']

        for tkn in tokens:
            if tkn in operands:
                match tkn:
                    case '+':
                        op1, op2 = nums.pop(), nums.pop()
                        nums.append(op1 + op2)
                    case '-':
                        op1, op2 = nums.pop(), nums.pop()
                        nums.append(op2 - op1)
                    case '*':
                        op1, op2 = nums.pop(), nums.pop()
                        nums.append(op1 * op2)
                    case '/':
                        op1, op2 = nums.pop(), nums.pop()
                        nums.append(int (op2 / op1))        # Assume that division between integers always truncates toward zero.
                        # nums.append(op2 // op1)       # rounds up to the next whole integer
            else:
                nums.append(int(tkn))
        return nums[-1]