class Solution:
    def countBits(self, n: int) -> List[int]:
        ## DP Approach *eye roll* -- optimal
        # Time: O(n) | Space: O(1)
        # dp = [0] * (n + 1)
        # offset = 1

        # for i in range(1, n + 1):
        #     if offset * 2 == i:
        #         offset = i
        #     dp[i] = 1 + dp[i - offset]
        # return dp

        
        ## DP x Bit Mask Approach -- optimal
        # Time: O(n) | Space: O(1)
        dp = [0] * (n + 1)
        for i in range(n + 1):
            print(f"{i=} | {(i >> 1)=}")
            dp[i] = dp[i >> 1] + (i & 1)        # make use of values we've already calculated in subsequent iteration to make it faster
            print(f"{dp=}")
        return dp