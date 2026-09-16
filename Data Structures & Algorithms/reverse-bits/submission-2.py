class Solution:
    def reverseBits(self, n: int) -> int:
        ## Bit manipulation I
        # Time and Space: O(1)
        res = 0
        for i in range(32):
            bit = (n >> i) & 1        # extract bit in the least significant bit and use id to construct res
            res |= (bit << (31 - i))  # |= or += works the same here since we're adding the shifted bit with res 
                                      # and shifting differently every iteration makes sure that we're not adding 
                                      # a 1 from res and a 1 from bit. Otherwise, it's much safer to use +=.
        return res