class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            # base case
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O":
                return

            board[r][c] = "T"
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in moves:
                dfs(r + dr, c + dc)

        # check the border of the board for the unsurrounded regions and convert O's to T's temporarily
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == "O":       # IMPORTANT to note the conditions to capture the unsurrounded regions properly
                    dfs(r, c)

        # go through the whole board and convert all O's to X's since the rest of the O's are surrounded by X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # go through the whole board for the 3rd time and convert all the T's to O's to get the final resulting board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
