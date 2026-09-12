class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = heights[-1]

        n = len(heights)
        res = [n-1]     # far right building will always have an ocean view
        # loop through list in reverse order - start from the 2nd to the last building
        for i in range(n-2, -1, -1):
            if heights[i] > maxHeight:
                res.append(i)
                maxHeight = heights[i]
        
        res.sort()
        return res