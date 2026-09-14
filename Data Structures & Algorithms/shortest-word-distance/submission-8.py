class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        wordMap = defaultdict(list) # since a word can show up multiple times

        for idx, word in enumerate(wordsDict):
            wordMap[word].append(idx)
        
        minDist = len(wordsDict) + 1    # arbitrary number
        for i1 in wordMap[word1]:
            for i2 in wordMap[word2]:
                minDist = min(minDist, abs(i1 - i2))
        return minDist