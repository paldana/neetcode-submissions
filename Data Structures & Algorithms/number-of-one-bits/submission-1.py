class Solution:
    def hammingWeight(self, n: int) -> int:
        ## Bit Mask I
        # Time: O(log n), Space: O(1)
        # count = 0
        # while n > 0:
        #     if n & 1:
        #         count +=1 
        #     n >>= 1
        # return count

        ## Bit Mask II
        # Time: O(1), Space: O(1)
        count = 0
        for i in range(32):
            if (1 << i) & n:
                count += 1
        return count