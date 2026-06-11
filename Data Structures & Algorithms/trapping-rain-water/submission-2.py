class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1                       # pointers
        maxL, maxR = height[l], height[r]   # max heights at respective pointers
        trappedWater = 0

        # Using 2 pointers method, we'll first retrieve the highest heights on both sides
        # that will be able to trap the rain water; Edges do not trap rain water!
        while l < r:
            if maxL < maxR:
                l += 1   # we increment right away since we already got the maxL from first element of list
                maxL = max(maxL, height[l])
                # if maxL > height[l], that means that water can be trapped beside it
                trappedWater += maxL - height[l]

            else:
                # Do the same for the right side if maxL >= maxR; move r inward
                r -= 1
                maxR = max(maxR, height[r])
                trappedWater += maxR - height[r]

        return trappedWater

# 2 Pointers Method
# Time: O(n), Space: O(1) 