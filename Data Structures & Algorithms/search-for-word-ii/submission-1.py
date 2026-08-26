class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # initialize the Trie with the words we're trying to look for in the board
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()
        
        def dfs(r, c, node, word):
            # check if the currenr r and c are not within range, have been visited, or not a child of the current node
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visited or
                board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isEndOfWord:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
