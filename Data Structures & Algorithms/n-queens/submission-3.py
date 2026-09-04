class Solution:
    # Backtracking + constraint checking solution - personal attempt
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]       # create an n x n board

        def backtrack(r):
            # base case
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                # check if current position is safe
                if isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
            
            return
        
        def isSafe(r, c, board):
            # check for Q in the rows above within the same column to check if the curr pos is safe
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1
            
            # check for Q in the pos diagonal (/)
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1

            # check for Q in the neg diagonal (\)
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            
            return True

        backtrack(0)
        return res