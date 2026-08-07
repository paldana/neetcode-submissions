class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i+1, len(nums)):
                if diff == nums[j]:
                    return [i, j]
                    
# Time complexity: O(n^2)
# Space complexity: O(1)
# Where n is the number of elements in nums.