## MinHeap Solution -- from NeetCode's video solution
# Time: O(n log(n)), Space: O(n)
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize) != 0:
            return False

        # frequency map - key: card number, value: count of cards
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            # iterate using the smallest card number in the heap in groups of groupSize
            # - need to have consecutive numbers starting from first
            for i in range(first, first + groupSize):       
                if i not in count:      # check if card number is available from the freq map
                    return False
                count[i] -= 1           # decrease the count for the card number i
                if count[i] == 0:       # check if there are any card number left in the stack 
                    if i != minH[0]:    # check if the number that we just used up is the same as the smallest number in the min heap
                        return False    # if not, then we won't be able to complete subsequent groups because i > minH[0] since we're planning to pop i from heap
                    heapq.heappop(minH) # pop from the min heap if card i has 0 count remaining
        return True
