class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []  # most recent val will be the min

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # if minVal is empty
        if not self.minStack:
            self.minStack.append(val)
        # if last value of minVal is bigger than new one, add it to the list
        elif self.minStack[-1] >= val:
            self.minStack.append(val)
            

    def pop(self) -> None:
        pop = self.stack.pop()
        # check if the popped value from the stack is the current minVal 
        if pop == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(self.minStack)
        return self.minStack[-1]

### Two Stack Method ###
# Time Complexity: O(1)
# Space Complexity: O(n)