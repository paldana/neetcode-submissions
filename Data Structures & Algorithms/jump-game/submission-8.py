## Greedy Solution
# Start from the end of the nums list and move the goal post as you iterate backwards
# Time: O(n), Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        # starting from 2nd to the last element, check if possible to get to current goal
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:     
                goal = i        # update goal to the current index to be used for the next iteration
        
        # if goal reached 0-index, then it's possible to complete the game
        return goal == 0        