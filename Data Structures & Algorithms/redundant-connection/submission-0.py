## DSU Solution

"""
Graph Theory
 For this problem, we weren't given the number of nodes in the problem. Only the number of edge pairs in the edges list.
 Since it was mentioned that we were initially given a graph with NO CYCLES and consisted of n - 1 edges, this means that
 we can infer that we have n nodes. 
 When another edge was introduced, the number of edges = number of nodes.

"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]     # +1 because we're creating a list representation of the vertex -> i.e. par[i] = parent of vertex i
        rank = [1] * (n+1)                  # and the +1 because it is 0-indexed

        # find the root parent of vertex, v
        def find(v):
            cur = v
            while cur != par[cur]:
                par[cur] = par[par[cur]]    # path compression algorithm to flatten the tree 
                cur = par[cur]
            return cur
        
        # merge the two vertices via their parents 
        def union(u,v):
            pu, pv = find(u), find(v)
            if pu == pv:    
                return False
            
            ## Union by Rank - Optimization
            if rank[pu] < rank[pv]:
                # swap pu and pv to have pu as the higher rank root vertex
                pu, pv = pv, pu
            par[pv] = pu        # make pu as the new root of pv
            rank[pu] += rank[pv]

            return True
        
        for u, v in edges:
            if not union(u, v):
                 # if we can't merge them - it means they're already within the same component/same root, then there's a cycle, so we can return these pair
                return [u, v]