class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack approach
        n = len(temperatures)
        res = [0] * n
        tempStack = []      # [temp, index]

        i = 0
        while i < n:
            while tempStack and temperatures[i] > tempStack[-1][0]: # check the top of the stack if the temperature is less than the current one
                _, j = tempStack.pop()           # pop and get the index from the stack
                res[j] = i - j                   # get the number of days it takes before it gets hotter than the jth day (j - i)
            tempStack.append([temperatures[i], i])
            i += 1
        
        return res