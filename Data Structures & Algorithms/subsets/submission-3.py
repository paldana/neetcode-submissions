class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## backtracking - dfs solution
        res = []
        subsets = []

        def dfs(i):
            
            if i >= len(nums):
                res.append(subsets.copy())
                return

            # decision to include nums[i] in the subset
            subsets.append(nums[i])
            dfs(i+1)

            # decision to not include nums[i] in the subset
            subsets.pop()
            dfs(i+1)
        
        dfs(0)
        return res