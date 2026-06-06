class Solution:
    def trap(self, height: List[int]) -> int:
        # Time: O(n), Space: O(1) -- 2 pointers
        if not height:
            return 0
        
        n = len(height)
        l, r = 0, n-1
        maxL, maxR = height[0], height[n-1]
        trappedWater = 0
        
        while l < r:
            if maxL < maxR:
                # since we already got the value of height[0] from initializing maxL
                l += 1
                maxL = max(maxL, height[l])
                trappedWater += maxL - height[l]
                
                # water = maxL - height[l]
                # if water > 0:
                #     trappedWater += water
                # maxL = max(maxL, height[l])
                
                
            else:
                r -= 1
                maxR = max(maxR, height[r])
                trappedWater += maxR - height[r]
        
        return trappedWater
                
            
        
        