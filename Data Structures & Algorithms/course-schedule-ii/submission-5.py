class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitedPath = set()
        processedCourse = set()
        roadmap = []

        def dfs(crs):
            if crs in visitedPath:
                return False
            
            if crs in processedCourse:
                return True
            
            visitedPath.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            roadmap.append(crs)
            visitedPath.remove(crs)
            processedCourse.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return roadmap
