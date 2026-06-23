class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}     # initialize the prerequisite hash map with empty lists
        for crs, pre in prerequisites:                  # key: course, val: list of prereqs
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)       # add the current course to the visit set and do DFS on it

            for pre in preMap[crs]:
                if not dfs(pre):    # run dfs on every prereq of the course
                    return False    # return False if dfs returns False -- cycle was detected
            
            visitSet.remove(crs)    # remove the course from the set as we've finished visiting it
            
            preMap[crs] = []        # re-set the value of prereq for the crs to [] if we didn't detect any 
                                    # cycle to prevent the code from running any further DFS on the course
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

# Cycle Detection via DFS
# Time & Space Complexity
# Time complexity: O(V+E)
# Space complexity: O(V+E)
# Where V is the number of courses and E is the number of prerequisites.