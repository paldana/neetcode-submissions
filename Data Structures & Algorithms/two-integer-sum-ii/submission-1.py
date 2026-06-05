class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1,2]
        
        res = []
        l, r = 0, len(numbers)-1 
        sums = []
        
        while l < len(numbers): 
            print(f"l: {l} | r: {r}")
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]   # since 1-indexed result is being asked in the problem
