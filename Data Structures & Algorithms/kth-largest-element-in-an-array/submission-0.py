class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

        # heapq.nlargest(k,nums)
        #    - returns a list of k largest values in nums. 
        #    - Since we only need the Kth value, this will be the last one on the list
        #    - So we have to do the [-1] at the end.