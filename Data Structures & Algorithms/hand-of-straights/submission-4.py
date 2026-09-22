## Hashmap Solution
# Time: O(n), Space: O(n)

from collections import Counter 


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize) != 0:
            return False
        
        count = Counter(hand)   # frequency map - key: card number, value: card count

        for num in hand:
            start = num
            # for a given number num, we first walk left to find the earliest possible start of its run
            # (we keep moving left while start - 1 still exists in the hand) - this ensures that we use up
            # smaller numbers than current num before building the next card group
            while count[start - 1]:
                start -= 1
            
            # once we know a possible start, we repeatedly form consecutive groups starting from that start
            while start <= num:
                while count[start]:
                    # build card group using the given groupPSize
                    for i in range(start, start + groupSize):
                        if not count[i]:    # if the expected number doesn't exist, then return False as we can't complete the grouping
                            return False
                        count[i] -= 1       # deduct count of the i card number
                start += 1
        return True
