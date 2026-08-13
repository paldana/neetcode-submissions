class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRow, nCol = len(matrix), len(matrix[0])

        ## 2-layer Binary Search ##
        # row layer -- find the specific row where the target can potentially be in
        top, bot = 0, nRow - 1
        # targetRow = 0
        currentRow = []
        while top <= bot:
            midRow = (top + bot) // 2
            currentRow = matrix[midRow]
            if currentRow[0] <= target and currentRow[-1] >= target:
                # targetRow = midRow
                # currentRow potentially contains the target, so break out of the while-loop
                break
            elif currentRow[0] > target:
                bot = midRow - 1
            else: # currentRow[-1] < target
                top = midRow + 1
        
        # col layer
        l, r = 0, nCol - 1
        # matRow = matrix[targetRow]
        while l <= r:
            mid = (l + r) // 2
            if currentRow[mid] < target:
                l = mid + 1
            elif currentRow[mid] > target:
                r = mid - 1
            else: # target found
                return True

        return False

# 2-Layer Binary Search Solution
# Time Complexity: O(log n * m), where m = row, n = col
# Space: O(1) 