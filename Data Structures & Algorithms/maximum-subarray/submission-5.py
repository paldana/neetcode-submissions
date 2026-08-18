class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        indexes = self.indexOfMaxSubArray(nums)
        return sum(nums[indexes[0]:indexes[1] + 1])


    def indexOfMaxSubArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxL, maxR = 0, 0
        maxSum = nums[0]
        L = 0

        currSum = 0
        for R in range(n):
            if currSum < 0:
                currSum = 0
                L = R
            
            currSum += nums[R]
            if currSum > maxSum:
                maxSum = currSum
                maxL, maxR = L, R

        return [maxL, maxR]