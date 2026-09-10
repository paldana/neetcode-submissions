class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ## two-pointer solution
        i1, i2 = -1, -1 
        minDistance = len(wordsDict) + 1    # arbitrary big number to indicate that we haven't measured the min distance

        # go through the wordDict and measure distance between the strings once they're both seen
        for idx, word in enumerate(wordsDict):
            if word == word1:
                i1 = idx
            elif word == word2:
                i2 = idx
            
            # compare distance between two words once they're both seen
            if i1 != -1 and i2 != -1:
                minDistance = min(minDistance, abs(i1 - i2))
            
        return minDistance