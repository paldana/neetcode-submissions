class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using Prefix and Suffix (postfix) - optimal method
        res = [1] * (len(nums))

        # 1st pass - left to right
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix         # product of all elements to the left
            prefix *= nums[i]

        # 2nd pass - right to left
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix       # product of all elements to the right
            postfix *= nums[i]
        return res

# Time and Space: O(n)