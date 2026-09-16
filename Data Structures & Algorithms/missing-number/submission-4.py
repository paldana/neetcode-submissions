class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## Sorting -- doesn't satisfy the required solution of Time Complexity: O(n) 
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]: 
        #         return i
        # return len(nums)

        ## Hash Set - Does not satisfy Space Complexity: O(1)
        num_set = set(nums)
        for i in range(len(nums) + 1):  # since we're expecting numbers from [0, n] and not n-1
            if i not in num_set:
                return i
        