class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []      # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            # loop - while stack is not empty 
            # and the top value of height is greater than the height than we just reached
            while stack and stack[-1][1] > h:
                # pop the height and calculate the max area of rectangle
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))    # i-index = width 
                start = index           # extend the start index to the index just popped
            
            # if top of stack is less than the current height, h, append to the end of stack
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

# Stack Method
# Time and Space: O(n)