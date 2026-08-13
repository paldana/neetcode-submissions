class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l + r) // 2

            if nums[mid] == target: 
                return mid
            
            # check left rotated portion
            if nums[l] <= nums[mid]:
                # if left portion is sorted, check if the target is within the left portion
                # if not, update the left boundary accordingly
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    # target is within the left sorted portion, so update right boundary
                    r = mid - 1
            
            # check right rotated portion
            else:
                # do the same to the right portion
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1

    # Binary Search (One Pass)
    # Time Complexity: O(log n)
    # Space Complexity: O(1)