class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # i is the pointer
        # cur is the current list of combinations visited
        # running total for the cur
        def dfs(i, cur, total):
            if total == target:
                # since we're going to continue using the cur list, we'd want to save
                # a COPY of it to the res; if we don't whatever the end content of cur after
                # the recursions will be the same ones showing up saved to res.
                # -- append in Python saves a reference to the original list object,
                #    hence why a copy of the same list is needed instead
                res.append(cur.copy())
                # res.append(cur)       # will cause issues => same as newCombo = cur; res.append(newCombo)
                # print(res)
                return

            if i >= len(nums) or total > target:
                return

            # perform DFS to navigate through the decision through (see neetcode video)
            # -- left side includes the current number i, right side doesn't
            cur.append(nums[i])          # add the current number to cur list for left side recursion
            dfs(i, cur, total + nums[i]) # nums[i] still included in the recursion (left side of decision tree)
            cur.pop()                    # removing the nums[i] we just appended for right side recursion
            dfs(i + 1, cur, total)       # do another recursion without the nums[i] (right side of decision tree)

        dfs(0, [], 0)
        return res


# Backtracking Solution
# Time & Space Complexity
# Time complexity: O(2*(t/m))
# Space complexity: O((t/m))
# Where t is the given target and m is the minimum value in nums.
