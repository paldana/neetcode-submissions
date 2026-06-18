class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []

        for s, d, weight in edges:
            adj[s].append([d, weight])
        
        shortest = {}       # map vertex -> distance of shortest path

        # Dijkstra's Algorithm is a Greedy BFS algo
        ## We start from the given source node and we do a BFS, always taking the edge
        ## that has the total shortest path
        minHeap = [[0, src]]        # initialize with a tuple of [0, src] 
                                    # where 0 is the distance for the src node to travel to src
                                    # -- will be used as the starting point of the BFS
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in shortest:      # if we've already visited the node, move on to the next in heap       
                continue
            shortest[n1] = w1

            # go through all the neighbor of the n1 node
            for n2, w2 in adj[n1]:
                if n2 not in shortest:                      # if n2 has already been visited
                    heapq.heappush(minHeap, [w1 + w2, n2])  # push the distance it needs to take to reach n2

        # set the vertices that are unreachable from src to -1 
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1 


        return shortest

            