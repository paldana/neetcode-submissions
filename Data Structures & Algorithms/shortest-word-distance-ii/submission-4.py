## two-pointer approach
#  time: O(n), space: O(1)
class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.wordArr = wordsDict

    def shortest(self, word1: str, word2: str) -> int:

        i1, i2 = -1, -1
        minDist = len(self.wordArr) + 1  # arbitrary large number
        for idx, word in enumerate(self.wordArr):
            if word == word1:
                i1 = idx
            elif word == word2:
                i2 = idx

            if i1 != -1 and i2 != -1:
                minDist = min(minDist, abs(i1 - i2))
        return minDist
