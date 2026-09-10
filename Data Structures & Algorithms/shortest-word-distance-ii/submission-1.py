class WordDistance:

    def __init__(self, words: List[str]):
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(words):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        min_diff = float("inf")
        
        for i1 in self.locations[word1]:
            for i2 in self.locations[word2]:
                min_diff = min(min_diff, abs(i1 - i2))

        return min_diff
