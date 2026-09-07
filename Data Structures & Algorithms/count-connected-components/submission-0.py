## Disjoint Set Union Solution - from NC video
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # representation lists, i.e. x is the node; par[x] = it's parent node (can be itself); rank[x] = number of child nodes connected to it, including itself
        par = [i for i in range(n)]     # parent representation list where initially each position is the parent of itself - [0, 1, 2, 3, ...] 
        rank = [1] * n                  # rank will be representing how many child nodes are connected to it (i.e. 1 means by itself, 2 means 1 child node is appended to that node)

        # Using Path Compression Algorithm to improve find() and flatten the tree - t.ly/uopgn
        # make the found root as parent of x (node); if x is a root of a subteree, then all other nodes under x also compresses
        def find(node):     # find the root parent of node
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]      # go up the chain
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:        # if they have the same parent, then we don't need to perform a union, so return 0
                return 0
            
            # perform union based on rank - let the lower ranked parent node be connected to the higher ranked node
            if rank[p2] > rank[p1]:
                # p2 will be the parent of p1
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                # p1 will be the parent of p2
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return 1    # to indicate that we've done a successful union of the 2 nodes

        res = n         # initialize to the number of unconnected nodes            
        for n1, n2 in edges:
            # everytime we get a successful union, we decrement res by 1
            res -= union(n1,n2)
        
        return res      # res will contain the remaining number of "unconnected" nodes = number of connected components
