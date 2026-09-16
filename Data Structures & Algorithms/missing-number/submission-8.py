class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## Math Solution - Time: O(n) | Space: O(1)
        # we know the expected total from the list of [0, n],
        # so subtract that value from total value of nums
        # to get the value of the missing number
        
        expectedSum = sum(range(len(nums) + 1))     # n + 1 to include n
        actualSum = sum(nums)
        return expectedSum - actualSum
