class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubIndices = self.indexOfMaxSubArray(nums)
        print(maxSubIndices)
        print(nums[maxSubIndices[0] : maxSubIndices[1]])
        return sum(nums[maxSubIndices[0] : maxSubIndices[1] + 1])

    # Return the left and right index of the max subarray sum,
    # assuming there's exactly one result (no ties)
    def indexOfMaxSubArray(self, nums: List[int]) -> List[int]:
        # Sliding Window variation of Kadane's Algorithm - Time: O(n); Space: O(1)
        maxSum = nums[0]
        curSum = 0
        maxL, maxR = 0, 0
        L = 0

        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R

            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R

        return [maxL, maxR]
