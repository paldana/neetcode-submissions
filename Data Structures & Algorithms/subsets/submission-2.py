class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res

    ## Iterative solution
    # Time: O(n * 2^n) | Space: O(n) for extra space; O(2^n) for the output list