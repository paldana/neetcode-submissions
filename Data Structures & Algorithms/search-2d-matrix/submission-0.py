class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2 layer binary search
        # since the arrays are sorted in increasing order and 2 dimensional

        top, bot = 0, len(matrix) - 1       # outer dimension - up and down
        l, r = 0, len(matrix[0]) - 1      # inner dimension - left to right

        mRow, mCol = 0, 0

        # find the row where the target number is
        while top <= bot:
            mRow = top + ((bot - top) // 2)

            if target >= matrix[mRow][0] and target <= matrix[mRow][-1]:
                break               # break out of the loop since we've found the potential row containing the target
            elif target < matrix[mRow][0]:
                bot = mRow - 1
            else:                   # target > matrix[mRow][-1]
                top = mRow + 1
            
        while l <= r:
            mCol = l + ((r - l) // 2)

            if matrix[mRow][mCol] == target:
                return True
            elif matrix[mRow][mCol] < target:
                l = mCol + 1
            else:                   # matrix[mRow][mCol] > target:
                r = mCol - 1
        
        return False
        
# Time complexity: O (log m*n), where m = row, n = col
# Space: O(1)
