# ## Practice Attempt - Recursion
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         n = len(nums)

#         # edge case - check if list is divisible by 2
#         if total % 2 != 0:
#             return False

#         target = total // 2

#         def dfs(idx, target):
#             # base case 1 - we got to the target number
#             if target == 0:
#                 return True

#             # base case 2 - if there are no more numbers left or if target becomes negative
#             if idx >= len(nums) or target < 0:
#                 return False

#             # decide if using the current index number or not
#             return dfs(idx + 1, target) or dfs(idx + 1, target - nums[idx])

#         return dfs(0, target)

## Practice Attempt - Top-Down Dynamic Programming - Memo x Recursion
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        # edge case - check if list is divisible by 2
        if total % 2 != 0:
            return False

        target = total // 2
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(idx, target):
            # base case 1 - we got to the target number
            if target == 0:
                return True

            # base case 2 - if there are no more numbers left or if target becomes negative
            if idx >= len(nums) or target < 0:
                return False

            # base case 3 - check memo cache if result already exists
            if memo[idx][target] != -1:
                return memo[idx][target]

            # decide if using the current index number or not
            memo[idx][target] = dfs(idx + 1, target) or dfs(idx + 1, target - nums[idx])
            return memo[idx][target]

        return dfs(0, target)
