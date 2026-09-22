# Practice - Greedy Approach (BFS using sliding window)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        l, r = 0, 0

        while r < n - 1:    # n-1 since we're okay not visiting the last element of the list
            farthest = 0
            for i in range(l, r + 1):   # iterate through the current sliding window range including r (hence + 1)
                farthest = max(farthest, i + nums[i])
            
            l = r + 1  
            r = farthest
            jumps += 1
        
        return jumps