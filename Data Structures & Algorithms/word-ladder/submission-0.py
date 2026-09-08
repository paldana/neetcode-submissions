class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case: check if the endword is in the wordList
        if endWord not in wordList:
            return 0

        """ Create an adjacency list of the words depending on the word patterns
        i.e. "hit" has 3 patterns: *it, h*t, hi*
             "hot" has 3 patterns: *ot, h*t, ho* 
             "dot" has 3 patterns: *ot, d*t, do*

            - these patterns will be saved in a dictionary of lists to add words from wordList that 
            would fall in their respective patterns

            nei["*it"] = [hit]
            nei["*ot"] = [hot, dot]
            nei["h*t"] = [hit, hot]
            nei["ho*"] = [hot]
            etc...

            Time complexity for creating this list: O(n * m * m) = O(n * m^2)
            - where n is the number of words in wordList and m is the length of each word
            -- 1st m is the number of times we move the * for the patterns
            -- 2nd m is for appending the word to the list in the neighbor dictionary
        """
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)


        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0