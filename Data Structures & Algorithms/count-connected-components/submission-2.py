class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n

        # retrieve all the adjacent nodes and save them in each node's respective array position 
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # go through the neighboring nodes until the adj list is exhausted to determine all the connected node that will be formed as a single component
        def dfs(i):
            for neighbor in adj[i]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)

        component = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                # go through the node's neighbors to determine all connected nodes that will form a single component
                dfs(i)
                # increase component after DFS completion
                component += 1
        
        return component

## DFS Solution
# Time and Space Complexity: O(n+e); n is num of nodes, e num of edges