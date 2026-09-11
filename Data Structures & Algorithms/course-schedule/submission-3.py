class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS with detection cycle solution
        # create a hashmap of all the courses' prerequisites
        preMap = {crs: [] for crs in range(numCourses)}  # key: course, value: [preReqs]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        seen = set()    # will be used to detect cycles in the prerequisites
        processed = set()

        def dfs(crs):
            # base cases
            if crs in seen:
                return False
            if crs in processed:
                return True
            seen.add(crs)
            # perform dfs on crs prerequisites
            for crsPre in preMap[crs]:
                if not dfs(crsPre):
                    return False            
                    
            seen.remove(crs)    # remove from seen as we've finished checking it
            processed.add(crs)
            # preMap[crs] = []    # clear the list for the said crs as we know it can be completed
            return True


        for crs in preMap.keys():     
        # for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



