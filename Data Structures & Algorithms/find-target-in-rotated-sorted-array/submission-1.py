class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l<=r:
            mid = l + (r - l)//2
            
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            if nums[mid] >= nums[l]:
                # target is not within the bounds of the left sorted portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1    # update to look for target in the other sorted portion
                else:
                    r = mid - 1    # update to look within the same sorted portion
            
            else:   # nums[mid] < nums[l]:
                # check if target is within the right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1   # update to look for target in the other sorted portion
                else:
                    l = mid + 1   # update to look within the same sorted portion
        
        return -1
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1)