class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        # i is the pointer to the current character in the word we're looking for
        def dfs(r, c, i):
            if i == len(word):
                return True

            # check boundary of the board 
            if (min(r, c) < 0 or                
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or   # check if the current char matches the current cell in the board      
                (r, c) in path):            # check if the current r,c has been visited before
                return False

            path.add((r, c))    # add the current position to the path set to be used for the subsequent recursions
            # do recursion throughout the adjacent positions in the board
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c)) # remove the position we just added as we're no longer visiting that position
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

# Backtracking (Hash set) Solution
# Time & Space Complexity
# Time complexity: O(m * 4^n)  - 4 is the number of DFS calls
# Space complexity: O(n)
# Where m is the number of cells in board and n is the length of the word.
