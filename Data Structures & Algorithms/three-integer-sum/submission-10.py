class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            # check if not the first element and val != prev num
            if i >= 1 and val == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                currSum = val + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1

                    # check for duplicates to skip
                    while (l<r) and nums[l] == nums[l-1]:
                        l += 1
            
        return res

# 2 pointer solution
# Time Complexity: O(n*log(n)) + O(n) --> O(n^2)
# Space Complexity: O(n)