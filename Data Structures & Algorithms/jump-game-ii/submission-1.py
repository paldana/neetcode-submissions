## BFS - Greedy Solution
# Time: O(n), Space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        # BFS using a "greedy window" instead of queue
        l, r = 0, 0     # reps range of indices reachable with the current number of jumps

        # find the farthest index we can reach in the next jump
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])   # get the farthest index reachable from current index i

            l = r + 1
            r = farthest
            jumps += 1      # increment jumps level by level once we get the farthest jump we can move to 
            
        return jumps
