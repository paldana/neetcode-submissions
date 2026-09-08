## DSU Solution - Union by Rank
class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, node):
        cur = node
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.par[pu] = pv
            self.rank[pv] += self.rank[pu]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return [u,v]
                