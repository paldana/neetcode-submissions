class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nROWS, nCOLS = len(board), len(board[0])
        
        # DFS
        def capture(r,c):
            # Base Case
            if (r not in range(nROWS) or 
                c not in range(nCOLS) or
                board[r][c] != "O"):
                return

            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        # capture every unsurrounded regions -> convert O's to T's temporarily
        for r in range(nROWS):
            for c in range(nCOLS):
                if (board[r][c] == "O" and 
                    (r in [0, nROWS - 1] or     # check if the cell is along the borders
                    c in [0, nCOLS - 1]) ):
                    capture(r,c)
                         
        # capture surrounded regions -> convert O's to X's
        for r in range(nROWS):
            for c in range(nCOLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # convert T's to O's back
        for r in range(nROWS):
            for c in range(nCOLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

## DFS Solution
# Time: O(m*n), m x n dimension of board
# Space: O(m*n) - recursive DFS stack can use up to O(m · n) call-stack space in the worst case, if the region forms a long chain.
#                The temporary 'T' markers are stored directly in the board and do not count as additional space.
#   Auxiliary space without the recursive stack is O(1)