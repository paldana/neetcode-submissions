class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using Division
        prod, zero_count = 1, 0

        # traverse the list to get the product of all non-zero numbers
        for num in nums:
            if num: 
                prod *= num
            else:
                zero_count += 1
        
        # if there's more than 1 zero, then return an array of all zeros
        if zero_count > 1:
            return [0] * len(nums)
        
        # set up result list with zeros
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            if zero_count:
                if not num:         # if we've found the index of the single 0 in the nums
                    res[i] = prod   # update the value to the prod of all the non-zero of the res[i]
            else:
                res[i] = prod//nums[i]  # '//' - floor division operator returns whole number; '/' will return float

        return res

# Time and Space complexity: O(n)
        