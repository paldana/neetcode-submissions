class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            if curr.word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        