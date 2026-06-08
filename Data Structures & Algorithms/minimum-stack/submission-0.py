class MinStack:

    def __init__(self):
        self.stack = []                     # stores encoded values (not the actual numbers)
        self.min = float('inf')             # stores the current minimum in the stack - actual num, not encoded

    def push(self, val: int) -> None:
        if not self.stack:                  # Pushing first element to the stack:
            self.stack.append(0)            # Push 0 (difference) as this will be the basis 
            self.min = val                  # for setting the min value
        else:      
            self.stack.append(val - self.min)   # Push val - min to the stack
            self.min = min(self.min, val)       # if val is the new minimum, update min.

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val < 0:                     # If this value is negative, it means the popped element was the minimum.
                self.min = self.min - val   # Restore the previous minimum using the encoded difference.

    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
            if top > 0:
                return top + self.min       # If the encoded value is positive, return encoded + min.
            else:
                return self.min             # If it's negative, the top actual value is simply min.

    def getMin(self) -> int:
        return self.min

# One Stack Method
# Time: O(1); Space: O(n) for the stack list