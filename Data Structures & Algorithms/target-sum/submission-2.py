## Dynamic Programming - Top-Down -- Memoization x Recursion
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}       # key: (i, cur_sum), value: number of ways to get cur_sum to target
        def backtrack(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)] 

            memo[(i, cur_sum)] = backtrack(i + 1, cur_sum + nums[i]) + backtrack(i + 1, cur_sum - nums[i])
            return memo[(i, cur_sum)] 

        return backtrack(0, 0)
