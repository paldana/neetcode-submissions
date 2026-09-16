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

        ## Bit Mask II - better 
        # Time: O(1), Space: O(1)
        # count = 0
        # for i in range(32):
        #     if (1 << i) & n:
        #         count += 1
        # return count

        ## Bit Mask II - better 
        # Time: O(1), Space: O(1)
        res = 0
        while n:
            res += 1 if n & 1 else 0
            n >>= 1
        return res