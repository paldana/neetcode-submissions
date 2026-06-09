class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = nums[0]  # pick the potentially min num of a sorted number arrayt

        while l <= r:
            if nums[l] < nums[r]:  # if array is sorted
                minNum = min(minNum, nums[l])
                break

            m = (l + r) // 2                # same as m = l + ((r-l) // 2)
            
            minNum = min(minNum, nums[m])
            if nums[l] <= nums[m]:
                # left side is sorted side, right side should contain min num
                l = m + 1
            else:           # if nums[m] < nums[r]:
                # right side is sorted side, left side should contain min num
                r = m - 1

        return minNum

# Time complexity: O(logn)
# Space complexity: O(1)