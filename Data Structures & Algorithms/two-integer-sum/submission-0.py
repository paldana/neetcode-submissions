class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashnum = {}

        for i, val in enumerate(nums):
            comp = target - val
            if comp in hashnum:
                return [i, hashnum[comp]] if hashnum[comp] > i else [hashnum[comp], i]
            else: 
                hashnum[val] = i
        
