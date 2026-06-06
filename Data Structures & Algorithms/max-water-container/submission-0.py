class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        
        for l in range(len(heights)):
            r = len(heights) - 1
            while l < r:
                currHeight = min(heights[l], heights[r])
                currLength = r - l
                currArea = currHeight * currLength
                maxA = max(maxA, currArea)
                r -= 1
        return maxA
            