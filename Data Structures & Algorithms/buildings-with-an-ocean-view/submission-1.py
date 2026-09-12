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
        
        # res.sort()      # O(n log(n))
        res.reverse()     # O(n)
        return res

## Personal attempt -- pretty straight forward
# Time complexity: O(nlogn) - because of sorting; O(n) if res.reverse() is used instead
# Space complexity: O(n)
# where
#     n is the number of elements in the input
#     res is the list of buildings with an ocean view