class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        eta = []        # less is faster

        for p, s in pairs:
            eta.append((target - p)/s)

            if len(eta) >= 2 and eta[-1] <= eta[-2]:
                eta.pop()
        
        return len(eta)