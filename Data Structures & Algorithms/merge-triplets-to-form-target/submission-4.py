## Practice - Greedy I Solution
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set()

        for t in triplets:
            # if any of the elements of current triplet, t, is greater than the 
            # any element of target, then we ignore this triplet as it won't be 
            # used to merge a triplet to form the target
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, num in enumerate(t):
                if num == target[i]:
                    valid.add(i)
            
        return len(valid) == 3