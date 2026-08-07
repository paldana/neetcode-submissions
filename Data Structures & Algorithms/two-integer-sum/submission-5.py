class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}    # key: number, val: index
        
        for i, num in enumerate(nums):
            diff = target - num

            if diff in map:
                return [min(i, map[diff]), max(i, map[diff])]
            else:
                map[num] = i  

