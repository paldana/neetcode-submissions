class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## bit manipulation
        res = 0 
        for num in nums:
            res = num ^ res
            print(res)
        return res