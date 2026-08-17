class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()     # for optimal backtracking algo

        # i = index
        # cur = list of current values in the path
        # total = sum of values in cur list
        def dfs(i, cur, total):
            # base case 1 - combination found
            if total == target:
                res.append(cur.copy())  # copy to create a separate list of cur to be appended to res, 
                                        # else it will be modified as we go through the recursions
                return
            
            # base case 2 - index out of bounds and total > target
            if i >= len(nums) or total > target:
                return

            ## non-optimal backtracking algo
            # cur.append(nums[i])
            # dfs(i, cur, total + nums[i])
            # cur.pop()
            # dfs(i + 1, cur, total)

            ## optimal backtracking algo
            for j in range(i, len(nums)):
                if total + nums[j] > target:    # no need to continue looking for possible combo if total + nums[j] > target
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()                       # remove recently added element to backtrack and retry next element
                

        dfs(0, [], 0)
        return res

## Optimal Backtracking Algo
# Time complexity: O(2^(t/m))
# Space complexity: O((t/m))
# Where t is the given target and m is the minimum value in nums.