class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k       # new k will be the index of the Kth largest in the list

        def quickSelect(l, r):
            # Use last element as the pivot point
            pivot, p = nums[r], l
            # go through
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]     # swap position with p
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]             # swap position p with the pivot

            # at this time, every number before pointer p (partition), is less than nums[p] - nums[0:p-1] < nums[p]
            # and every number after pointer p is greater than nums[p] - nums[p+1:len(nums)-1] > nums[p]
            # if current pivot position is greater than the new K
            if p > k:       
                # run quickSelect recursively with updated pointers, 
                # focusing on the left side of the partition to find the target Kth largest element
                return quickSelect(l, p - 1)
            elif p < k:
                # likewise if p < k
                return quickSelect(p + 1, r)
            else:
                # we've found the Kth largest element 
                return nums[p]

        return quickSelect(0, len(nums) - 1)    # -1 because list is 0-indexed

## Quick Select Solution ##
# Time complexity: O(n) - worst case O(n^2)
# Space complexity: O(n) - due to recursion stack, where n is the length of nums