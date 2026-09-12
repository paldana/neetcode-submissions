## Brute Force - DFS
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def current_island_is_unique():
            for other_island in unique_islands:
                if len(other_island) != len(current_island):
                    continue

                ## For-else block -- else will only execute if the for-loop completed the sequence and didn't encounter a break statement
                for cell_1, cell_2 in zip(current_island, other_island):
                    if cell_1 != cell_2:
                        break
                else:
                    # if it completes the whole sequence and everything matches, returns False since it is not a unique island
                    return False    
        
            return True

        # Do a DFS to find all cells in the current island.
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            current_island.append((row - row_origin, col - col_origin))     # using row and col origin is key to determining if island is unique
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Repeatedly start DFS's as long as there are islands remaining.
        seen = set()
        unique_islands = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = []     # will contain the offset coordinates from the row and col origins so the islands can be compared with one another
                row_origin = row
                col_origin = col
                dfs(row, col)
                if not current_island or not current_island_is_unique():
                    continue
                unique_islands.append(current_island)
        print(unique_islands)
        return len(unique_islands)

## Brute Force - DFS
# NeetBot Complexity Analysis
#    Time complexity: O(n*m + k*i*c)
#    Space complexity: O(n*m)

# Where:
#     n is the number of rows in the grid
#     m is the number of columns in the grid
#     k is the number of islands found
#     i is the average number of cells per island
#     c is the number of previously stored unique islands
