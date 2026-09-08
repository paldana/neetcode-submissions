## BFS Solution - personal attempt
# Time complexity: O(nL)
# Space complexity: O(nL)
# Variables: n = number of words in the input (wordList plus beginWord), L = length of each word

from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case: if endWord is not in the wordList, return 0
        if endWord not in wordList:
            return 0

        # by treating words as vertices, 
        # create a neighbor dict using word patterns that can be derived from each word in the wordList
        # - this dict will be the adjacency list
        nei = defaultdict(list)
        wordList.append(beginWord)  # since beginWord is not in the wordList originally
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[(i+1):]
                nei[pattern].append(word)
        
        
        # Perform BFS to the neighboring vertices starting from the beginWord
        q = deque([beginWord])
        visited = set([beginWord])
        transCount = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return transCount
                
                visited.add(w)
                
                # go through the current word's adjacency list
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[(i+1):]
                    for neighbor in nei[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            transCount += 1         # increase count every after level/word
        
        return 0
