class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []  # list of tuples: (index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, ht = stack.pop()
                maxA = max(maxA, ht * (i - idx))
                start = idx

            stack.append((start, h))
        
        for i, h in stack:
            maxA = max(maxA, h * (len(heights) - i))
        
        return maxA