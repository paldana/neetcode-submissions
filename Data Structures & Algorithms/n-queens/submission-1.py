class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Knowing that we can only put 1 queen every row
        # We need 3 sets to keep track of the attacked positions
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            ## Base Case
            if r == n:
                res.append(
                    ["".join(row) for row in board]
                )  # since the board consists of separate lists per r,c location
                # and we expect the output to be lists of list of strings
                # containing the possible layout i.e. [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
                return

            # check if the current position is in an attacked position
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
            return

        backtrack(0)
        return res
