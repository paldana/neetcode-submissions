## Stack Approach
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i, h in enumerate(heights):
            # iterate through stack and 
            # check if previously checked idx is higher than the current h.
            # if not, remove the stack shorter or equal to h
            while stack and heights[stack[-1]] <= h:    
                stack.pop()
            stack.append(i)
        return stack