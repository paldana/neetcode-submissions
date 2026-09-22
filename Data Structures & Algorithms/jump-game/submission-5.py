## Personal Attempt - Dynamic Programming - Recursion x Memoization
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums) - 1:
                return True
            if i < len(nums) - 1 and nums[i] == 0:
                return False

            for j in range(1, nums[i]+1):
                if dfs(i + j):
                    memo[i+j] = True
                    return True
            memo[i] = False
            return False
            
        return dfs(0)