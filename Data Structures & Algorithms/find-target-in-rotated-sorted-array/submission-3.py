class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # find pivot point by doing a binary search
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        # will converge to l being the pivot point/beginning of the unrotated sorted array
        pivot = l

        # need to do binary search on one side or both side of the array if necessary
        def binary_search(l: int, r: int):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:  # nums[m] > target
                    r = m - 1
            return -1

        res = binary_search(pivot, len(nums) - 1)
        if res != -1:
            return res
        else:
            return binary_search(0, pivot - 1)
