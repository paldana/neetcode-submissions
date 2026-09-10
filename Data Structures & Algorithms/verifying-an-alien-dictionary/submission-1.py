class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienDictOrder = {}  # key: character, val: index from the order
        # extract order indexes
        for idx, c in enumerate(order):
            alienDictOrder[c] = idx

        # shorter way
        # alienDictOrder = {c:idx for idx, c in enumerate(order)}

        # go through the words and compare 2 words at a time
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                # check if index of w1 exceeds that of w2, meaning the order of words is invalid 
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if alienDictOrder[w1[j]] > alienDictOrder[w2[j]]:
                        return False
                    break   # break out of the inner for-loop since we've confirmed that the words are in correct order
                            # so move on to the next pair to be compared
        return True

## Comparing Adjacent Words
# Time complexity: O(c), where c is the total number of characters across all words in the input list.
# Space Complexity: O(1)
        