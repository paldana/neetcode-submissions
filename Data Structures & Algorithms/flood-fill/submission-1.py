class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        targetColor = image[sr][sc]  # int value of the starting pt of the flood fill

        # if new color is the same as the original color, return original image
        if targetColor == color:
            return image 
            
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != targetColor:
                return

            if image[r][c] == targetColor:
                image[r][c] = color  # set the new color

            # perform recursion on adjacent columns
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image

# DFS Solution
# Time & Space Complexity
# Time complexity: O(m∗n)
# Space complexity: O(m∗n)