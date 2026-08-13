class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # mid = (r - l) // 2        # incorrect way of calculating middle
            # mid2 = (r+l)//2           # correct way
            mid = l + ((r - l) // 2)    # alternative correct way    
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return -1
