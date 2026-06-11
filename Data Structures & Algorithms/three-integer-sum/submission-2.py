class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):    # outer-loop to get the first val in the triplets
            if a > 0:
                break       # all remaining numbers are positive, hence no possible solution

            if i > 0 and a == nums[i - 1]:
                continue    # Skip duplicate values for the first number since we don't want 
                            # duplicate triplets in the result

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])   # add valid triplets in the results list
                    l += 1                  # move the pointers accordingly
                    r -= 1
                    
                    # keep moving pointer until there are no duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

# 2 Pointers Method
# Time: O(n^2) + O(n * log(n)) = O(n^2), --> O(n * log(n)) for sorting
# Space: O(m),  plus the space used by the sorting algorithm.
# This excludes the space used for the output list.
# If the output list is included, the space is O(m), which is O(n^2) in the worst case.
#  - Where m is the number of unique triplets and n is the length of the given array.