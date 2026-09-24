## Dynamic Programming - Bottom-Up approach - Space Optimized
# Time complexity: O(n * m)
# Space complexity: O(m)
# where n is the number of elements in nums and m is the sum of all the elements in the array.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1   # 0 sum -> 1 way -- 1 way to sum to zero with first 0 elements

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]