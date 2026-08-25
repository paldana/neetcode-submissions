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
                if c == ".":
                    # recursion of search method
                    # go through all the children of curr node
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                if c not in curr.children:
                    return False
                
                curr = curr.children[c]
            return curr.endOfWord
        
        return dfs(0, self.root)

# DFS Solution
# Time complexity : O(n) for addWord() and search()
# Space Complexity: O(t + n), where n is length of string, t istotal number of TrieNodes created in the Trie