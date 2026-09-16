class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## Math Solution - Time: O(n) | Space: O(1)
        # we know the expected total from the list of [0, n],
        # so subtract that value from total value of nums
        # to get the value of the missing number
        
        # expectedSum = sum(range(len(nums) + 1))     # n + 1 to include n
        # actualSum = sum(nums)
        # return expectedSum - actualSum

        ## Math Approach 2
        # Instead of computing two separate sums, we can combine both ideas into a 
        # single running calculation, which keeps the logic clean and avoids overflow issues in some languages.
        # This approach uses basic arithmetic, making it easy to understand and language-independent.
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res