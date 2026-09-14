"""
    Create a new data structure named TrieNode to create a Prefix Tree
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()   # create a new child TrieNode if the char DNE yet
            curr = curr.children[c]
        curr.isWord = True      # once we've reached the end of the word to be inserted, set the curr TrieNode's isWord to True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            if curr.isWord:
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
        