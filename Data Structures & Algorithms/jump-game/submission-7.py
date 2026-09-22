## Greedy Solution
# Start from the end of the nums list and move the goal post as you iterate backwards
# Time: O(n), Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0