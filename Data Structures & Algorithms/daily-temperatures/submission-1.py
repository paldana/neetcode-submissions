class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## Stack Approach
        n = len(temperatures)
        res = [0] * n
        tempStack = []     # [temp, index]
        i = 0

        while i < n:
            while tempStack and temperatures[i] > tempStack[-1][0]:
                temp, j = tempStack.pop()
                res[j] = i - j
            tempStack.append([temperatures[i], i])
            i += 1

        return res


