class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## brute force
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]
        # return []

        ## Hash map (one-pass)
        compMap = {}    # key: complement number to get target, value: index 

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in compMap:
                return [compMap[comp], i]
            else:
                compMap[nums[i]] = i
        return []