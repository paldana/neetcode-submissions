class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    ## Brute Force
        for i in range(len(nums)):
            duplicateFlag = False
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    duplicateFlag = True
                    break
            if not duplicateFlag:
                return nums[i]
            