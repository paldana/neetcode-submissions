class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            self.wordsDict[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        minDistance = len(self.wordsDict) + 1
        for i1 in self.wordsDict[word1]:
            for i2 in self.wordsDict[word2]:
                minDistance = min(minDistance, abs(i1 - i2))
        return minDistance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
