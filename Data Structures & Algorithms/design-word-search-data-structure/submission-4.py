class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(idx, root):
            curr = root
            for i in range(idx, len(word)):
                c = word[i]

                if c == ".":        # if char is a wildcard, go through the every child node of the current TrieNode and do DFS to all of them
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    else:
                        return False
                    
                if c not in curr.children:
                    return False

                curr = curr.children[c]   
            return curr.endOfWord

        return dfs(0, self.root)
                        



