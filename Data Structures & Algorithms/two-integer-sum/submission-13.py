class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Brute Force
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]
        # return []
        
        ## Hash map Approach
        hashMap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashMap:
                return [hashMap[comp], i]
            hashMap[nums[i]] = i

        return []
