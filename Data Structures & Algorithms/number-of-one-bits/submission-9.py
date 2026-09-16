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
        
        ## Bit Mask I - better Time Complexity??
        # Time: O(1), Space: O(1)
        ## How is this better when it's pretty much the same? IDK fuck this BS.
        # res = 0
        # while n:
        #     res += 1 if n & 1 else 0
        #     n >>= 1
        # return res

        ## Bit Mask II - better 
        # Time: O(m), Space: O(1), where m = 32 iterations for the whole 32-bit digits given
        # count = 0
        # for i in range(32):
        #     if (1 << i) & n:
        #         count += 1
        # return count

        ## Bit Mask III - Optimal 
        # Time: O(k), Space: O(1), where k = number of 1 bit in n
        # res = 0
        # print(bin(n))
        # while n:
        #     n &= n - 1      # removes the rightmost 1 bit from n ==> n = n & (n - 1)
        #     print(bin(n))
        #     res += 1
        # return res

        """
        ex. n   = 11 -> 1011
            n-1 = 10 -> 1010
            n & (n-1) = 1010 --> 10
            
            n   = 10 -> 1010
            n-1 =  9 -> 1001
            n & (n-1) = 1000 --> 8

            n   =  8 -> 1000
            n-1 =  7 -> 0111
            n & (n-1) = 0000 --> 0
        """

        ## Built-in Python function
        # Time: O(1), Space: O(1)
        return bin(n).count('1')
