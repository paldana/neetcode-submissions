## Kadane's Algorithm Approach - Dynamic Programming
# Time: O(n)
# Space: O(1)
""" The idea is to maintain 2 numbers, curMin and curMax, and go through the nums list to see what values are 
    generated in these 4 scenarios:
        1. num is + and multiplies curMax and curMin as normal to get a higher/lower product value
        2. num is - and multiplies curMax and curMin, where curMax will be negative and curMin will be positive, if also negative
        3. num is 0 and both curMax and curMin will be 0
        4. num is + and will reset either or both curMin and curMax
    
    Also keep track of the res variable to get the max product after going through the list
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1       # Keep track of curMin for tracking the smallest negative numbers

        ## if previous num is 0, the algorithm above will reset the curMax and curMin to the next num if they are both 0s
        for num in nums:
            tmp = curMax * num                              # store curMax * num to temp since curMax will be updated 
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)            # if current num is negative, curMin might be the new max if they're both negative
            res = max(res, curMax)
        return res
