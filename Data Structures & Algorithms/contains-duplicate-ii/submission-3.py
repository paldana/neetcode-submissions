class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                j = seen[num]
                if i != j and abs(i-j) <= k:
                    return True
                else:
                    # update the last time we've seen this index in the hash
                    seen[num] = i
            else: 
                seen[num] = i
        
        return False