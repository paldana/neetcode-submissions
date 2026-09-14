class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        res = len(wordsDict) + 1    # arbitrarily large number 
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                res = min(res, abs(i1 - i2))
            
        return res