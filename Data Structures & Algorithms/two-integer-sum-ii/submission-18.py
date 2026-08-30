class Solution:
    ## Two pointer solution - Non-Binary Search
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     n = len(numbers)
    #     if n == 2:
    #         return [1, 2]

    #     l, r = 0, n - 1
    #     while l < r:
    #         sum = numbers[l] + numbers[r]
    #         if sum == target:
    #             return [l + 1, r + 1]
    #         elif sum < target:
    #             l += 1
    #         else:
    #             r -= 1
    #     return []

    ## Binary Search
    # Time: O(n log(n) )
    # Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 2:
            return [1, 2]

        for i in range(n):
            comp = target - numbers[i]
            
            l, r = i+1, n - 1
            while l <= r:
                mid = (l + r) // 2
                if comp == numbers[mid]:
                    return [i + 1, mid + 1]
                elif comp > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
