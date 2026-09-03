class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(i, subset):
            if i >= len(nums):
                res.add(tuple(subset))
                return

            # decision to add number to the subset
            subset.append(nums[i])
            backtrack(i+1, subset)

            # decision to NOT add number to the subset
            subset.pop()
            backtrack(i+1, subset)

            return
        
        nums.sort()     # so duplicates are next to each other
        backtrack(0, [])

        # return list(res)
        return [list(r) for r in res]