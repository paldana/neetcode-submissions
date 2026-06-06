class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        l, r = 0, len(heights)-1

        while l < r:
            # Calculate area by getting current height and length of potential container
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)

            # move pointers based on the heights we've seen -> move shorter height inward
            if heights[l] <= heights[r]:
                l += 1          # move l pointer to the right to look for a higher height
            else:
                r -= 1          # vice versa for right pointer

        return max_area

# Time: O(n); Space: O(1)