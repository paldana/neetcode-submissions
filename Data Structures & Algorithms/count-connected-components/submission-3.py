## DFS Solution - 2nd go
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list which will contain the directly connected nodes to node, x (i.e. node[x] = [y, z, ...])
        adj = [[] for _ in range(n)]
        # create a visit array to indicate if the node has been visited -- visit[node]
        visit = [False] * n

        # go through the list of edges to retrieve adjacent nodes
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # go through each of the adjacent nodes and mark them as visited. Will finish after going through the node's adjacency list.
        def dfs(node):
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)

        # go through the adjacency list to determine how many components are connected
        component = 0
        for i in range(n):
            if not visit[i]:
                # go through the adjacenct nodes using DFS
                dfs(i)
                component += 1

        return component


