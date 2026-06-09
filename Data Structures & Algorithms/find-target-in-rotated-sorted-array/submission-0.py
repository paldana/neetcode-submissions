class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            
            # check left side of rotated array
            if nums[m] >= nums[l]:
                # target is not within the left sorted array
                if target > nums[m] or target < nums[l]:
                    l = m + 1       # update l to check the other side
                else:
                    r = m - 1

            else:   # else nums[m] > nums[r]
                # check right side of rotated array
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
