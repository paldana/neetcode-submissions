## DFS Solutionn - Cycle Detection -- personal attempt
# Time complexity: O(E∗(V+E))
# Space complexity: O(V+E)
# Where 
# V is the number of vertices and 
# E is the number of edges in the graph.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [ [] for _ in range(n + 1)]
        visited = [False] * (n + 1)   # can just be declared within the for loop below and it will still be used by DFS just fine

        def dfs(vertex, par):
            if visited[vertex]:     # base case - if we've visited the node before, there's a cycle
                return True
            
            visited[vertex] = True  # mark the current vertex as visited

            for neighbor in adj[vertex]:
                if neighbor == par: # skip parent vertex
                    continue
                if dfs(neighbor, vertex):
                    return True

            return False

        for u, v in edges:
            # add the edges on the list as we go through the edges list
            adj[u].append(v)
            adj[v].append(u)
            
            # recreate the visited array every iteration to check if the newly added edge creates a cycle
            visited = [False] * (n + 1)

            if dfs(u, -1):
                return [u,v]        # return the recent edge if a cycle is detected
        
        return []