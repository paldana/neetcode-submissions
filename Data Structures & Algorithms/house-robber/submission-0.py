class Solution:
    def rob(self, nums: List[int]) -> int:
        # Intuition: at any house, we only care about
        # -- the best result up to the previous house
        # -- the best result up to the house before that
        # So instead of storing everything, we just keep two variables and update them as we move forward.
        
        # For each house:
        # -- Either skip it → keep previous best
        # -- Or rob it → current money + best from two steps back
        # Pick the maximum.

        # rob1 best up to house i - 2 -- house prev to prev house
        # rob2 best up to house i - 1 -- previous house
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...] - max amount of money at index, i
        for num in nums:
            # newRob(temp) = max(rob2, rob1 + currentHouseValue)
            temp = max(num + rob1, rob2)   # choose if you want to get either rob1 and n or rob2 
            rob1 = rob2                    # update rob1 and rob2 pointers
            rob2 = temp                    
        # by the time we get to the last house, rob2 will contain the max val that can be robbed
        return rob2

## Dynamic Programming (Space Optimized)
# Time: O(n) | Space: O(1)