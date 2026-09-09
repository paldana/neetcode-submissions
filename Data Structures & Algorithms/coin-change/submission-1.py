class Solution:
    ## BFS Approach -- pretty straightforward
    # Time Complexity: O(n * t)
    # Space Complexity: O(n)
    # - where n = len(coins), t = given amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        seen = set()
        numCoins = 0
        q = deque([0])

        while q:
            numCoins += 1
            for _ in range(len(q)):
                amt = q.popleft()
                for coin in coins:
                    nxtAmt = amt + coin
                    if nxtAmt == amount:
                        return numCoins

                    if nxtAmt in seen or nxtAmt > amount:
                        continue
                    seen.add(nxtAmt)
                    q.append(nxtAmt)
        
        return -1   # if impossible to give valid number of coins 