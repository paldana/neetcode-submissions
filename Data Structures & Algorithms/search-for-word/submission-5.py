class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # in order to determine if the word exists in the board,
        # we'll have to go through each board chars until we find 
        # a match to the word char for char -- DFS solution
        nRows, nCols = len(board), len(board[0])
        visited = set()

        # r = row, c = col, i = current index    
        def dfs(r, c, i):
            # base case 1 - if index matches length of word = word is found! 
            if i == len(word):
                return True

            # base case 2 - check if within board bounds and if element has been seen
            if (r < 0 or r >= nRows or
                c < 0 or c >= nCols or
                board[r][c] != word[i] or
                (r,c) in visited):
                return False
            
            # DFS operations
            visited.add((r,c))
            # visit adjacent elements in the board using dfs recursion
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            visited.remove((r,c)) # remove element added to get back to original state (backtrack)
            return res

        for r in range(nRows):
            for c in range(nCols):
                if (dfs(r, c, 0)):
                    return True
        return False
        
