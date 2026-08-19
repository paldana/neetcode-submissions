class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Brute Force
        # n = len(nums)
        # for i in range(n):
        #     comp = target - nums[i]
        #     for j in range(i+1, n):
        #         if nums[j] == comp:
        #             return [i,j]
        # return []

        ## Hashmap solution
        hmap = {}   # key: num, val: index
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hmap:
                return [min(hmap[comp], i), max(hmap[comp], i)]
            hmap[nums[i]] = i
        return []
