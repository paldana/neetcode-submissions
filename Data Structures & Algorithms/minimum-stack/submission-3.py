class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return
        minNum = self.stack[0]
        for n in self.stack:
            minNum = min(minNum, n)

        return minNum 

# Brute Force
# Time and Space Complexity: O(n) for getMin(), O(1) for rest of the ops