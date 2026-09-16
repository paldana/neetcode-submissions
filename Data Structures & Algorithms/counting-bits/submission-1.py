class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        ## Using built-in Python function
        # Time: O(n log(n)) | Space: O(n), where n is the input integer representing the range up to which bit counts are computed
        # for i in range(n+1):
        #     res[i] = bin(i).count('1')
        # return res

        for i in range(n+1):
            num, count = i, 0
            while num:
                num &= num - 1
                count += 1
            res[i] = count
        return res