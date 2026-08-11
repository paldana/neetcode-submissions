class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [0 for i in range(n)] 
        rightMax = [0] * n      # same as above - simpler

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i-1])
        
        rightMax[n-1] = height [n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        trapped_water = 0
        for i in range(n):
            trapped_water += min(leftMax[i], rightMax[i]) - height[i]
        
        return trapped_water

# Prefix and Suffix Array Solution
# Time Complexity: O(n)
# Space Complexity: O(n)