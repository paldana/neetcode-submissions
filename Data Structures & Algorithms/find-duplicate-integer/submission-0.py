class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #sorted_nums = sorted(nums)
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)