## Dynamic Programming - Top Down - memo x recursion
# Time: O(n^3)
# Space: O(n^2)
#   where n is the number of elements in the input
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # add 1s to the edges of the nums array
        memo = {}  # key: (l, r), value: num of coins at (l,r)
        # l and r are index windows for which we are solving subproblems for -- rewatch NC's video for more details

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            memo[(l, r)] = 0
            # go through the remaining nums list
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                memo[(l, r)] = max(memo[(l, r)], coins)
            return memo[(l, r)]

        return dfs(1, len(nums) - 2)
