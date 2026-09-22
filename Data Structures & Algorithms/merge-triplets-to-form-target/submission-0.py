## Greedy Solution
# Time: O(n), Space: O(1), where n is len(triplets)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()    # will contain indices - if by the end of the for-loop below we have 3 values,
                        # it means that we can merge at least 2 triplets to get the target triplet

        for t in triplets:
            # filter out triplets that are not valid since they have values higher than the target triplet
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # go through the triplets list and check if any of the triplets matches the target values and indices
            for i, v in enumerate(t):
                if v == target[i]:  # if there's a match from the target triplet, store the found index in the good set
                    good.add(i)
        return len(good) == 3