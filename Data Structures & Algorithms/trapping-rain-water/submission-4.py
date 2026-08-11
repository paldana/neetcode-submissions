class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r: 
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                trapped_water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                trapped_water += maxR - height[r]
        
        return trapped_water

# 2 Pointers Method
# Time: O(n), Space: O(1) 