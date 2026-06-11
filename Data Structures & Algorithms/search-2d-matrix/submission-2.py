class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2D-layer Binary Search - sorted arrays
        l, r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        targetRow = 0
        # locate the row that can possibly contain the target 
        # then perform a binary search in the same row to find the target

        while top <= bottom:
            mid = (bottom + top)//2

            if matrix[mid][0] > target:     # if val of the least element in the row < target
                bottom = mid - 1            # move the bottom pointer to point to the smaller val rows
            elif matrix[mid][-1] < target:  # highest val in row < target
                top = mid + 1               # move top pointer to point to the higher val rows
            else:
                # we've found our rows
                targetRow = mid
                break
        
        # now perform binary search in the row
        while l <= r:
            m = (r + l) // 2
            midVal = matrix[targetRow][m]
            if target == midVal:
                return True
            elif midVal < target:
                l = m + 1
            else:
                r = m - 1
        
        return False

# Time complexity: O (log m*n), where m = row, n = col
# Space: O(1)
