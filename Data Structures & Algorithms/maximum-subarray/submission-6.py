class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        maxL, maxR = 0, 0   # will be the indices of the max subarray
        L, R = 0, 0
        while R < len(nums):
            # if curSum is negative, reset it to 0 and update L pointer to where R is
            if curSum < 0:
                curSum = 0
                L = R
            
            curSum += nums[R]

            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R
            
            R += 1
        # return maxL and maxR if the answer we're looking for is the indices of the subarray or the subarray itself
        
        return maxSum