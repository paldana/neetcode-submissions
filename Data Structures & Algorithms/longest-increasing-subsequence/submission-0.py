## Dynamic Programming (Bottom-Up) - II
# Time: O(n^2), Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)   # each element is a subsequence of 1

        # iterate the nums list backwards to 
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)    # update the current idx in LIS to add the LIS of the subsequent element + 1 to include current idx's count
        return max(LIS)     # return the max value in the list

