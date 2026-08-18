class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS with Cycle Detection Solution
        # create a prereq map - key: course, val: [prereqs]
        preMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # cycle set = tracks the current DFS path for cycle deteciton
        # visited set = tracks fully processed courses
        cycle, visited = set(), set()
        roadmap = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)          # add crs in the DFS path's cycle set
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)       # remove from the set after processing path
            visited.add(crs)        # add crs to the fully processed set
            roadmap.append(crs)     # add to the resulting list - deepest course in the path gets appended first,
                                    # meaning it needs to be taken first in order to take subsequent courses
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return roadmap

# DFS with Cycle Detection Solution
# Time complexity: O(V+E)
# Space complexity: O(V+E)
# Where V is the number of courses and E is the number of prerequisites.
