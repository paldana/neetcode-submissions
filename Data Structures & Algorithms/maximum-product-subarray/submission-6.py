class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minProd, maxProd = 1, 1

        for num in nums:
            temp = num * maxProd
            maxProd = max(num * maxProd, num * minProd, num)
            minProd = min(temp, num * minProd, num)
            res = max(res, maxProd)
        
        return res
