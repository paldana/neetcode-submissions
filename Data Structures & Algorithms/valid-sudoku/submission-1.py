from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)              # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]
                if curr_val == '.':
                    continue
                
                if (curr_val in rows[r] or
                    curr_val in cols[c] or
                    curr_val in squares[(r//3, c//3)]):
                    # if the current value is already seen in the hash sets, 
                    # return False there shouldn't be any duplicates for valid Sudoku boards
                    return False
                
                # save the current value to the hash sets of seen values
                rows[r].add(curr_val)
                cols[c].add(curr_val)
                squares[(r//3, c//3)].add(curr_val)

        return True

# Time complexity: O(n^2); Space Complexity: O(n^2) - because of the hash sets