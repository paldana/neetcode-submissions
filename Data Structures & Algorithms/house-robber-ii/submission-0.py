class Solution:
    def rob(self, nums: List[int]) -> int:
                            # except the first house    # except the last house
        return max(nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
                   # in case there's only 1 house in the list 
                   
    # solution from House Robber I problem - https://neetcode.io/problems/house-robber/solution
    def rob_helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2 
            rob2 = newRob

        # will contain maximum val we can rob from nums list
        return rob2