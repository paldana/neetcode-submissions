class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]

        iMap = {}   # key: number; value: index of num in numbers list
        
        for i, num in enumerate(numbers):
            comp = target - num
            print (f"i:{i} | num: {num} | comp: {comp}")

            if comp in iMap:
                return [iMap[comp], i+1]
            else:
                iMap[num] = i+1
        
        return []