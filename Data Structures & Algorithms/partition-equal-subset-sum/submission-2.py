## DP - Top-Down - Memoization x Recursion 
# Time and Space : O(n * target), where n is len(nums) and target is sum of nums elements divided by 2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:      # if total sum of numbers in nums is not divisible by 2, then we can't partition into 2 equal subsets
            return False

        n = len(nums)
        target = total // 2
        memo = [[-1] * (target + 1) for _ in range(n + 1)]  # 2D Dynamic Programming
        
        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]

            memo[i][target] = (dfs(i + 1, target) or
                               dfs(i + 1, target - nums[i]))
            return memo[i][target]

        return dfs(0, target)