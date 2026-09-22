## Dynamic Programming - Memoization x Recursion 
# Time: O(n^2)
# Space: O(n)
# where n is the number of elements in nums
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        
        # finds the length of the longest increasing subsequence starting at index i
        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            LIS = 1         # for current index
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))      # the +1 is for including the current index
            
            # LIS will be 1 if no subsequent numbers are less than current index
            memo[i] = LIS   # cache the LIS at index i
            return LIS

        # run dfs on every num in nums and return the longest subsequence that will be found
        return max(dfs(i) for i in range(len(nums)))