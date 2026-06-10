class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm - Time: O(n); Space: O(1)
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            # if previous curSum is negative, do not add it to the next element
            curSum = max(curSum, 0)
            curSum += n

            # check if the curSum is now bigger than the maxSum
            maxSum = max(maxSum, curSum)
        return maxSum