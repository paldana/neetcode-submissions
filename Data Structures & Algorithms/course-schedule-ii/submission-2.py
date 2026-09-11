class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle = set()       # will be used to detect cycle in the course path
        visited = set()     # will be used to indicate if the course's prerequisites have been checked and there are no cycles detected
        roadmap = []        # will contain a valid order of courses to take to finish all courses

        def dfs(crs):
            # Base cases
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)      # add to current course path

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)   # remove from current course path
            visited.add(crs)    # add to visited so we don't have to run DFS on this crs
            roadmap.append(crs) # add crs to roadmap - deepest course will be appended first - Post Order traversal

            return True


        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return roadmap

