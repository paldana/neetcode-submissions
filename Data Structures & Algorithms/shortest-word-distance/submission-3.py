class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        indexes = defaultdict(list)

        for index, word in enumerate(wordsDict):
            indexes[word].append(index)

        min_dist = float('inf')
        for i in indexes[word1]:
            for j in indexes[word2]:
                min_dist = min(abs(i - j), min_dist)

        return min_dist

## Two-Pointer Solution
# Time: O(n + m * k) - n is len(wordsDict), m = num of occurences of word1, k = num of occurences of word2
# Space: O(n)