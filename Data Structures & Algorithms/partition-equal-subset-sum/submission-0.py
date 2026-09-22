## Dynamic Programming
# During interviews, to best come up with this solution, start with Brute Force -> Memoization -> DP
# Time: O()
# Space: O()

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums) % 2):  # if not 0, then it is not possible to have 2 subsets whose sums are equal
            return False

        dp = set()      # will contain all the possible sums in the nums list
        dp.add(0)       # base case - if we don't add any nums, we'll always get a sum 0
        target = sum(nums) // 2     # target value

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()      # since we're going to be updating dp, we'll need to create a new one (or clone dp) 
            for t in dp:
                if (t + nums[i]) == target:     # if we've found a subset that generated the sum equal to the target, cut the code short and return True
                    return True
                nextDP.add(t + nums[i]) # add new values in sum set as we go through the nums list
                nextDP.add(t)           # add back the values already in dp set
            dp = nextDP                 # update dp with the newly added sums in the nextDP

        return True if target in dp else False
