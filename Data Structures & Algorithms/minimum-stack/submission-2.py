class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.minStack.append(val)
        
        self.stack.append(val)
        
        if self.min >= val:             # check if val is <= than current min
            self.min = val
            self.minStack.append(val)   # top of minStack will be the new min

    def pop(self) -> None:
        pop = self.stack.pop()
        if self.minStack[-1] == pop:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# 2 Stack Method
# Time: O(1); Space: O(n) for the stack lists