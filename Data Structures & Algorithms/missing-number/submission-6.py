class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n            # important to initialize with n since we're expecting values from 0 to n
        for i in range(n):
            xorr ^= i ^ nums[i]     # after going through the list, all values from 0 to n-1 will be cancelled out by XOR ^ if it's in the list
        return xorr         # will return the missing number 

## Bit Manipulation - Time: O(n),  Space: O(1)