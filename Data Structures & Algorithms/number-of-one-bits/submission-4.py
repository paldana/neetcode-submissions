class Solution:
    def hammingWeight(self, n: int) -> int:
        ## Bit Mask I
        # Time: O(log n), Space: O(1)
        count = 0
        while n:
            if n & 1:
                count +=1 
            n >>= 1
        return count
        
        ## Bit Mask I - better Time Complexity??
        # Time: O(1), Space: O(1)
        ## How is this better when it's pretty much the same?
        # res = 0
        # while n:
        #     res += 1 if n & 1 else 0
        #     n >>= 1
        # return res

        ## Bit Mask II - better 
        # Time: O(1), Space: O(1)
        # count = 0
        # for i in range(32):
        #     if (1 << i) & n:
        #         count += 1
        # return count

