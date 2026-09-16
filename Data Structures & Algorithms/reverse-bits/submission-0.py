class Solution:
    def reverseBits(self, n: int) -> int:
        print(bin(n))
        ## brute force - just go through the whole 32-bit integer and turn 0s into 1s and vice versa
        binary = ""
        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"
        
        print(binary)
        # convert the binary string to integer by going through the string in reverse order 
        # bit by bit and shifting left by i times
        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= 1 << i
        return res