## Hash By Local Coordinates Approach
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        unique_islands = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            """
            Note: all the variables other than r and c are enclosed variables (declared in the enclosing function calling the dfs),
                  hence we can still use them inside the dfs. 

                You need "nonlocal" only when you reassign the enclosing variable inside the nested function:
                def outer():
                    current_island = []

                    def dfs():
                        nonlocal current_island
                        current_island = [(0, 0)]  # reassignment

                However, mutating the object is different from reassigning the variable:
                def outer():
                    current_island = []

                    def dfs():
                        current_island.append((0, 0))  # mutation: no nonlocal needed
                Here, current_island still refers to the same list. You are changing the list’s contents, not making the name refer to a new list.
            """
            # base case - if r,c out of range, visited, or water
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            current_island.add((r - r_origin, c - c_origin))    # key to determine the size pattern for each island
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                
                current_island = set()
                r_origin, c_origin = r, c  # will be used within dfs
                dfs(r, c)
                if current_island:
                    # frozenset is used because it's hashable, so the current_island set can be added to another set
                    unique_islands.add(frozenset(current_island))   # duplicate shapes of islands will be filtered out

        return len(unique_islands)

## Hash By Local Coordinates Approach
# Time complexity: O(R*C)
# Space complexity: O(R*C)
# Where
#   R is the number of rows in the grid
#   C is the number of columns in the grid