class Solution:
    def hammingWeight(self, n: int) -> int:
        ## Bit Mask I
        count = 0
        while n > 0:
            if n & 1:
                count +=1 
            n >>= 1
        return count

        ## Bit Mask II
        