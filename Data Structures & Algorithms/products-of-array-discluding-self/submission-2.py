class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force - time: O(n^2)
        res = []
        i = 0
        while i < len(nums):
            j = 0
            prod = 1
            while j < len(nums):
                if j != i:        
                    prod = prod * nums[j]
                j += 1

            res.append(prod)
            i += 1
        
        return res

