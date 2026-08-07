class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## division method
        # look for zeros in nums; if there are more than 1 zero, return all 0
        # get prod of all non-zero num in nums; this will be used to get result

        res = [0] * len(nums)
        prod, zeros = 1, 0

        for i, val in enumerate(nums):
            if val:
                prod *= val
            else:
                zeros += 1
        
        if zeros > 1:
            return res
        
        for i, val in enumerate(nums):
            if zeros:
                if not val:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // val
        
        return res

