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


    # # Return the left and right index of the max subarray sum,
    # # assuming there's exactly one result (no ties)
    # def indexOfMaxSubArray(self, nums: List[int]) -> List[int]:
    # # Sliding Window variation of Kadane's Algorithm - Time: O(n); Space: O(1)
    #     maxSum = nums[0]
    #     curSum = 0
    #     maxL, maxR = 0, 0
    #     L = 0

    #     for R in range(len(nums)):
    #         if curSum < 0:
    #             curSum = 0
    #             L = R
            
    #         curSum += nums[R]
    #         if curSum > maxSum:
    #             maxSum = curSum
    #             maxL, maxR = L, R
        
    #     return [maxL, maxR]