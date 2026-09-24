## Dynamic Programming - Bottom-Up approach
# Time complexity: O(n * m)
# Space complexity: O(n)
# where n is the number of elements in nums and m is the sum of all the elements in the array.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]   # +1 for offsetting to get to last index of len(nums) 
        dp[0][0] = 1        # (0 elements used, cur_sum = 0) -> 1 way  - 1 way to sum to zero with first 0 elements

        for i in range(n):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count

        return dp[n][target]