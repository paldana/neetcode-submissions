class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {crs: [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        processed = set()
        def dfs(crs):
            if crs in visited:
                return False    # cycle detected

            if crs in processed:
                return True

            visited.add(crs)
            # go through prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            processed.add(crs)  
            visited.remove(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True


