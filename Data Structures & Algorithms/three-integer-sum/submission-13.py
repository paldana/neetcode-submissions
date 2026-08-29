class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res

## Hashmap Solution
# Time: O(n^2) + O(n * log(n)) = O(n^2), 
#       --> O(n * log(n)) for sorting
# Space: O(n),  plus the space used by the sorting algorithm.
# This excludes the space used for the output list.
# O(n) is used for the frequency map.
#  If the output list is included, the space is O(n+m), which is O(n^2) in the worst case.rray.