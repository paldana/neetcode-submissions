class Solution:
    ## Backtracking + Constraint Checking Solution
    # Time: O(n!)
    # Space: O(n^2)
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."

        backtrack(0)
        return res

    def isSafe(self, r: int, c: int, board):
        # check for any queens in the same col in the rows above 
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        # check for any queens in the negative diagonal (\)
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # check for any queens in the positive diagonal (/)
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        
        # return true if current position is a safe 
        return True