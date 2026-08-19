class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Brute Force
        res = []
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == comp:
                    return [i,j]
        return []
