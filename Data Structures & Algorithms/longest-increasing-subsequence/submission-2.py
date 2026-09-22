## Dynamic Programming - Memoization x Recursion 
# Time: O(2^n) - 2 decisions every recursion
# Space: O(n)
# where n is the number of elements in nums
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        
        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            LIS = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))
            
            memo[i] = LIS
            return LIS

        return max(dfs(i) for i in range(len(nums)))