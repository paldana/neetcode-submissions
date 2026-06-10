class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane's Algorithm - Time: O(n); Space: O(1)
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        # if globmax > 0 condition is to account for the edge case 
        # wherein all the numbers in the list are negative and 
        # if both total and globMin are negative,
        # it will return the wrong answer (total - globMin) 
        return max(globMax, total - globMin) if globMax > 0 else globMax