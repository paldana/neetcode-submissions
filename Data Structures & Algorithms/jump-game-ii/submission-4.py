## DP Top-Down - Memo x Recursion 
# Time: O(n^2), Space: O(n), where n is len(nums)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [float('inf') for _ in range(n)]

        def dfs(idx):
            # base case 1 - check if we've reached the end of the list (-1 because 0-indexed)
            if idx == n - 1:
                return 0
            
            # base case 2 - check if current idx steps is 0 -> return arbitrarily large number so we won't get this when we use min()
            if idx < n and nums[idx] == 0:
                return float('inf')
            
            # base case 3 - check memo cache
            if memo[idx] != float('inf'):
                return memo[idx]
            
            end = min(n - 1, idx + nums[idx])   # set the end of the for-loop to which ever is smaller between the available steps at current index or the end of list
            res = float('inf')      # arbitrary large number since we're looking for the min number of jumps needed to complete the game
            for i in range(idx + 1, end + 1):
                res = min(res, 1 + dfs(i))      # +1 is the number of jump per recursion and we're going to get the min. number of jumps possible
            memo[idx] = res
            return res

        return dfs(0)