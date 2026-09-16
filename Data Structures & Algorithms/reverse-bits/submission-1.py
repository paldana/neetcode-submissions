class Solution:
    def reverseBits(self, n: int) -> int:
        ## Bit manipulation I
        # Time and Space: O(1)
        res = 0
        for i in range(32):
            bit = (n >> i) & 1        # extract bit in the least significant bit and use id to construct res
            res |= (bit << (31 - i))
        return res