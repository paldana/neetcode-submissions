## Greedy II - (Optimal)
# Time: O(n), Space: O(1), where n is len(triplets)

'''
Instead of collecting indices in a set, we can think more directly:
    To reach target[0], we need at least one triplet where:
        - the first value equals target[0]
        - the other two values do not exceed the target
    Similarly for target[1] and target[2]

If we can independently satisfy all three positions using valid triplets, then merging those triplets will exactly form the target.
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False       # Initialize three boolean flags
        
        for t in triplets:
            # |= bitwise OR assignment operator -- will keep x TRUE once it is TRUE -> x = x or (conditions)
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])    # we only care about the x pos of triplet, etc below.    
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
            
            if x and y and z:   # if all true, then it's possible to merge 2 triplets to get to target
                return True
        return False