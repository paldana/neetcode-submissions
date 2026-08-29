class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):

            if num > 0: break

            if i >= 1 and num == nums[i - 1]:   # check if the current num is the same as the previous num in nums
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]
                if total < 0:
                    l += 1  # increase the left pointer
                elif total > 0:
                    r -= 1
                else:   # found a possible combination that equals to 0
                    res.append([num, nums[l], nums[r]])   # append the combo in res
                    # keep going through the list for other possible combo
                    l += 1                      
                    r -= 1
                    while nums[l] == nums[l -1] and l < r:  # skip duplicate nums
                        l += 1
        return res
