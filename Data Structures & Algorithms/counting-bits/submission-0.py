class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        # Using built-in Python function
        for i in range(n+1):
            res[i] = bin(i).count('1')
        return res