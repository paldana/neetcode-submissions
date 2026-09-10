class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ## two-pointer solution - Optimal Solution
        ## time: O(n), space: O(1)
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

        ## Hashmap solution
        # time: O(n + k*m), n = len(wordsDict), k, m = num of occurence of word1 and word2, respectively
        # space: O(n)
        # iMap = defaultdict(list)    # will contain all the indices where each word are found

        # for i, word in enumerate(wordsDict):
        #     iMap[word].append(i)
        
        # minDist = len(wordsDict) + 1

        # for i1 in iMap[word1]:
        #     for i2 in iMap[word2]:
        #         minDist = min(minDist, abs(i1 - i2))
        
        # return minDist
