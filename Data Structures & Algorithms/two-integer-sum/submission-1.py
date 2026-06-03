class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # addressing the assumption that every input has exactly 2 indices that satisfies the condition
        if len(nums) == 2:
            return [0, 1]
        
        for i, val in enumerate(nums):
            comp = target - val

            if comp in nums:
                # get index of the comp in nums
                i_comp = nums.index(comp)
                # check if the index of comp is not the same as the current i in case it's the same value
                if i_comp == i:
                    try:
                        # try looking for another index in nums and start from the first occurence of the val
                        i_comp = nums.index(comp, i_comp + 1)
                    except ValueError:
                        continue
                return [i, i_comp]

# Non-Hash map solution
        


