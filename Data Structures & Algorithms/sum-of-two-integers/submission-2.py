class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF       # mask to keep our int to 32 bits
        max_int = 0x7FFFFFFF    # largest 32-bit signed integer

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        # after the loop, a holds the 32-bit result
        
        # if a is within the signed range, return directly
        # otherwise, convert from unsigned 32-bit to a negative signed valut and return it
        return a if a <= max_int else ~(a ^ mask)