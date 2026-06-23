class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        # adj = [[] for _ in range(n)]      # this will create a hashmap list too?
        adj = { i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        # node = current node, prev = previous node
        def dfs(node, prev):
            if node in visit:
                return False        # loop detected, so return False

            visit.add(node)
            # check for neighboring nodes
            for nei in adj[node]:
                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False
            return True

        # return True if the recursion didn't detect any cycles AND the len of visited nodes == n,
        # meaning there's no isolated nodes
        return dfs(0, -1) and len(visit) == n

# Cycle Detection (DFS)
# Time & Space Complexity
# Time complexity: O(V+E)
# Space complexity: O(V+E)
# Where V is the number vertices and E is the number of edges in the graph.